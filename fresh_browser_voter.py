"""
FRESH BROWSER VOTER - Closes and reopens browser each vote
Complete fresh session every time
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime

class FreshBrowserVoter:
    def __init__(self, worker_id):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.worker_id = worker_id
        self.vote_count = 0
        self.success_count = 0
        self.fail_count = 0
        
    def create_driver(self):
        """Create fresh Chrome browser"""
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Random user agent
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        ]
        options.add_argument(f'user-agent={random.choice(user_agents)}')
        
        driver = webdriver.Chrome(options=options)
        
        # Remove webdriver property
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver
    
    def vote_once_fresh(self):
        """Single vote with FRESH browser (close and reopen)"""
        driver = None
        try:
            print(f"[Worker {self.worker_id}] Opening fresh browser...")
            
            # Create NEW browser
            driver = self.create_driver()
            
            # Human delay after opening
            time.sleep(random.uniform(1, 2))
            
            # Load page
            print(f"[Worker {self.worker_id}] Loading voting page...")
            driver.get(self.url)
            
            # Human delay (reading page)
            time.sleep(random.uniform(2, 4))
            
            # Check if redirected
            current_url = driver.current_url
            if 'tech' not in current_url.lower():
                print(f"[Worker {self.worker_id}] BLOCKED - Redirected to homepage")
                return False
            
            # Wait for form
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'form'))
                )
            except:
                print(f"[Worker {self.worker_id}] No form found")
                return False
            
            # Extra wait for labels
            time.sleep(2)
            
            # Find and click option
            print(f"[Worker {self.worker_id}] Finding option...")
            labels = driver.find_elements(By.TAG_NAME, 'label')
            
            if len(labels) == 0:
                print(f"[Worker {self.worker_id}] No options found")
                return False
            
            found = False
            for label in labels:
                try:
                    text = label.text.lower()
                    if 'ashutosh' in text and 'pratap' in text:
                        print(f"[Worker {self.worker_id}] Clicking: {label.text}")
                        time.sleep(random.uniform(0.5, 1.5))
                        label.click()
                        found = True
                        break
                except:
                    continue
            
            if not found:
                print(f"[Worker {self.worker_id}] Option not found")
                return False
            
            # Human delay after selecting
            time.sleep(random.uniform(0.5, 1.5))
            
            # Find submit button
            print(f"[Worker {self.worker_id}] Submitting vote...")
            try:
                submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
            except:
                try:
                    submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
                except:
                    print(f"[Worker {self.worker_id}] No submit button")
                    return False
            
            # Human delay before clicking submit
            time.sleep(random.uniform(0.3, 0.7))
            submit.click()
            
            # Wait for response
            time.sleep(3)
            
            # Check if redirected after submit
            current_url = driver.current_url
            if 'tech' not in current_url.lower():
                print(f"[Worker {self.worker_id}] BLOCKED after submit")
                return False
            
            # Check result
            page_source = driver.page_source.lower()
            if 'thank' in page_source or 'success' in page_source:
                print(f"[Worker {self.worker_id}] SUCCESS!")
                return True
            else:
                print(f"[Worker {self.worker_id}] Vote failed")
                return False
            
        except Exception as e:
            print(f"[Worker {self.worker_id}] Error: {str(e)[:50]}")
            return False
            
        finally:
            # ALWAYS close browser after vote
            if driver:
                print(f"[Worker {self.worker_id}] Closing browser...")
                driver.quit()
                time.sleep(1)  # Wait before next browser
    
    def run_infinite(self):
        """Keep voting with fresh browser each time"""
        print(f"[Worker {self.worker_id}] Starting FRESH BROWSER voting...")
        print(f"[Worker {self.worker_id}] Browser closes and reopens each vote")
        print(f"[Worker {self.worker_id}] Press Ctrl+C to stop")
        print()
        
        try:
            while True:
                self.vote_count += 1
                start_time = time.time()
                
                print(f"\n[Worker {self.worker_id}] ========== VOTE #{self.vote_count} ==========")
                
                success = self.vote_once_fresh()
                
                elapsed = time.time() - start_time
                
                if success:
                    self.success_count += 1
                    status = "✓ SUCCESS"
                    delay = random.randint(5, 10)
                else:
                    self.fail_count += 1
                    status = "✗ FAILED"
                    delay = random.randint(10, 20)
                
                # Summary
                print(f"\n[Worker {self.worker_id}] {status} | Time: {elapsed:.1f}s")
                print(f"[Worker {self.worker_id}] Total: {self.vote_count} | Success: {self.success_count} | Fail: {self.fail_count}")
                print(f"[Worker {self.worker_id}] Waiting {delay}s before next vote...")
                print(f"[Worker {self.worker_id}] {datetime.now().strftime('%H:%M:%S')}")
                
                # Wait before next vote
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n\n[Worker {self.worker_id}] Stopped by user")
        finally:
            print(f"\n[Worker {self.worker_id}] ===== FINAL STATS =====")
            print(f"[Worker {self.worker_id}] Total votes: {self.vote_count}")
            print(f"[Worker {self.worker_id}] Successful: {self.success_count}")
            print(f"[Worker {self.worker_id}] Failed: {self.fail_count}")
            if self.vote_count > 0:
                success_rate = (self.success_count / self.vote_count) * 100
                print(f"[Worker {self.worker_id}] Success rate: {success_rate:.1f}%")


if __name__ == "__main__":
    import sys
    
    worker_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    print("="*70)
    print(f"FRESH BROWSER VOTER - Worker {worker_id}")
    print("="*70)
    print("\nHow it works:")
    print("  1. Opens Chrome browser")
    print("  2. Votes")
    print("  3. CLOSES browser completely")
    print("  4. Waits 5-10 seconds")
    print("  5. Opens NEW browser")
    print("  6. Repeat")
    print("\nThis avoids detection by starting fresh each time!")
    print("\nSpeed: ~3-5 votes per minute per browser")
    print("Press Ctrl+C to stop")
    print("="*70)
    print()
    
    voter = FreshBrowserVoter(worker_id)
    voter.run_infinite()
