"""
EMERGENCY ULTRA-FAST VOTER
Maximum speed solution - bypasses nonce by getting it fresh each time
Uses asyncio + aiohttp with proper nonce extraction
"""
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime

class EmergencyVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.ajax_url = "https://blizzardproductionhouse.com/wp-admin/admin-ajax.php"
        
    async def get_fresh_nonce(self, session):
        """Get a fresh nonce from the page"""
        async with session.get(self.url) as response:
            text = await response.text()
            
            # Extract nonce from page
            nonce_match = re.search(r'"nonce"\s*:\s*"([^"]+)"', text)
            if nonce_match:
                return nonce_match.group(1)
            
            # Fallback: look for any nonce pattern
            nonce_match = re.search(r'nonce["\']?\s*[:=]\s*["\']([a-f0-9]{10,})["\']', text, re.I)
            if nonce_match:
                return nonce_match.group(1)
            
            return None
    
    async def submit_vote_with_nonce(self, session, vote_num):
        """Get fresh nonce and submit vote"""
        try:
            # Get fresh nonce
            nonce = await self.get_fresh_nonce(session)
            
            # Prepare form data
            form_data = {
                'form_id': '353',
                'page_id': '7',
                'form_type': 'poll',
                'current_url': self.url,
                'action': 'forminator_submit_form_poll',
                '_wp_http_referer': '/tech/',
                'answers-0': 'ashutosh-pratap-singh',
            }
            
            if nonce:
                form_data['_wpnonce'] = nonce
                form_data['forminator_nonce'] = nonce
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://blizzardproductionhouse.com',
                'Referer': self.url,
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
            
            async with session.post(self.ajax_url, data=form_data, headers=headers) as response:
                text = await response.text()
                
                try:
                    import json
                    resp_json = json.loads(text)
                    success = resp_json.get('success', False)
                    return vote_num, success, resp_json.get('data', text[:100])
                except:
                    return vote_num, False, text[:100]
                    
        except Exception as e:
            return vote_num, False, str(e)[:100]
    
    async def vote_batch_async(self, num_votes):
        """Submit votes with fresh sessions"""
        print(f"Starting {num_votes} votes with async HTTP...\n")
        
        successful = 0
        failed = 0
        start_time = time.time()
        
        # Create separate session for each vote to avoid cookie conflicts
        async def vote_with_session(vote_num):
            async with aiohttp.ClientSession() as session:
                return await self.submit_vote_with_nonce(session, vote_num)
        
        tasks = [vote_with_session(i+1) for i in range(num_votes)]
        results = await asyncio.gather(*tasks)
        
        for vote_num, success, message in results:
            if success:
                successful += 1
                print(f"[{vote_num}] ✓")
            else:
                failed += 1
                print(f"[{vote_num}] ✗ {message}")
        
        elapsed = time.time() - start_time
        
        print(f"\n{'='*70}")
        print(f"Successful: {successful}/{num_votes}")
        print(f"Failed: {failed}/{num_votes}")
        print(f"Time: {elapsed:.1f}s ({num_votes/elapsed:.1f} votes/sec)")
        print(f"{'='*70}")
        
        return successful


# OPTION 2: Multi-threading with Selenium (most reliable)
from concurrent.futures import ThreadPoolExecutor
import threading

class ThreadedSeleniumVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.lock = threading.Lock()
        self.success_count = 0
        self.fail_count = 0
        
    def vote_once_fast(self, vote_num):
        """Optimized single vote"""
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        
        driver = webdriver.Chrome(options=options)
        
        try:
            driver.set_page_load_timeout(10)
            driver.get(self.url)
            
            # Quick wait for form
            time.sleep(1.5)
            
            # Find and click option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            for label in labels:
                if 'ashutosh' in label.text.lower() and 'pratap' in label.text.lower():
                    driver.execute_script("arguments[0].click();", label)
                    break
            
            time.sleep(0.3)
            
            # Submit
            submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            driver.execute_script("arguments[0].click();", submit)
            
            time.sleep(2)
            
            if 'thank' in driver.page_source.lower() or 'success' in driver.page_source.lower():
                with self.lock:
                    self.success_count += 1
                print(f"[{vote_num}] ✓")
                return True
            else:
                with self.lock:
                    self.fail_count += 1
                print(f"[{vote_num}] ✗")
                return False
                
        except Exception as e:
            with self.lock:
                self.fail_count += 1
            print(f"[{vote_num}] ✗ {str(e)[:30]}")
            return False
        finally:
            driver.quit()
    
    def vote_parallel(self, total_votes, max_workers=10):
        """Run votes in parallel"""
        print(f"Starting {total_votes} votes with {max_workers} workers...\n")
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            list(executor.map(self.vote_once_fast, range(1, total_votes + 1)))
        
        elapsed = time.time() - start_time
        
        print(f"\n{'='*70}")
        print(f"Successful: {self.success_count}/{total_votes}")
        print(f"Failed: {self.fail_count}/{total_votes}")
        print(f"Time: {elapsed:.1f}s ({total_votes/elapsed:.1f} votes/sec)")
        print(f"{'='*70}")


if __name__ == "__main__":
    print("="*70)
    print("EMERGENCY ULTRA-FAST VOTER")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    print("\nChoose method:")
    print("1. Async HTTP (FASTEST - 50+ votes/sec, may fail due to nonce)")
    print("2. Parallel Selenium (RELIABLE - 2-5 votes/sec, WORKS)")
    print("="*70)
    
    choice = input("\nSelect (1/2): ").strip()
    
    if choice == '1':
        votes = int(input("How many votes? "))
        voter = EmergencyVoter()
        asyncio.run(voter.vote_batch_async(votes))
        
    elif choice == '2':
        votes = int(input("How many votes? "))
        workers = int(input("Parallel browsers (5-20 recommended)? "))
        voter = ThreadedSeleniumVoter()
        voter.vote_parallel(votes, workers)
        
    else:
        print("Invalid choice")
