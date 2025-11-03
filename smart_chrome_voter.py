"""
SMART CHROME VOTER - Human-like behavior to avoid detection
Uses Chrome with anti-detection measures
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime

class SmartChromeVoter:
    def __init__(self, worker_id):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.worker_id = worker_id
        self.vote_count = 0
        self.success_count = 0
        self.fail_count = 0
        self.block_count = 0
        
    def create_driver(self):
        """Create Chrome browser with anti-detection"""
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
    
    def human_delay(self, min_sec=0.5, max_sec=2.0):
        """Random delay to mimic human behavior"""
        time.sleep(random.uniform(min_sec, max_sec))
    
    def vote_once_smart(self, driver):
        """Single vote with human-like behavior"""
        try:
            # Load page
            driver.get(self.url)
            self.human_delay(1, 2)
            
            # Check if redirected to homepage (BLOCKED)
            current_url = driver.current_url
            if 'tech' not in current_url.lower():
                print(f"[Worker {self.worker_id}] BLOCKED - Redirected to homepage!")
                print(f"[Worker {self.worker_id}] Waiting 60 seconds before retry...")
                self.block_count += 1
                time.sleep(60)  # Long wait after being blocked
                return False
            
            # Wait for form
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'form'))
                )
            except:
                print(f"[Worker {self.worker_id}] No form - page blocked")
                return False
            
            # Human-like delay (reading the page)
            self.human_delay(2, 4)
            
            # Find and click option (with human delay)
            labels = driver.find_elements(By.TAG_NAME, 'label')
            if len(labels) == 0:
                print(f"[Worker {self.worker_id}] No options found")
                return False
            
            for label in labels:
                try:
                    text = label.text.lower()
                    if 'ashutosh' in text and 'pratap' in text:
                        # Human-like delay before clicking
                        self.human_delay(0.3, 0.8)
                        label.click()  # Use regular click, not JavaScript
                        break
                except:
                    continue
            
            # Human delay after selecting
            self.human_delay(0.5, 1.5)
            
            # Find and click submit
            try:
                submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
            except:
                try:
                    submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
                except:
                    print(f"[Worker {self.worker_id}] No submit button")
                    return False
            
            # Human delay before submitting
            self.human_delay(0.3, 0.7)
            submit.click()  # Use regular click
            
            # Wait for response
            time.sleep(3)
            
            # Check if redirected after submit (BLOCKED)
            current_url = driver.current_url
            if 'tech' not in current_url.lower():
                print(f"[Worker {self.worker_id}] BLOCKED after submit - Bot detected!")
                self.block_count += 1
                return False
            
            # Check result
            page_source = driver.page_source.lower()
            success = 'thank' in page_source or 'success' in page_source
            
            return success
            
        except Exception as e:
            print(f"[Worker {self.worker_id}] Error: {str(e)[:50]}")
            return False
    
    def run_infinite(self):
        """Keep voting with smart delays"""
        print(f"[Worker {self.worker_id}] Starting SMART infinite voting...")
        print(f"[Worker {self.worker_id}] Using human-like behavior")
        print(f"[Worker {self.worker_id}] Press Ctrl+C to stop")
        
        driver = self.create_driver()
        
        try:
            while True:
                self.vote_count += 1
                start_time = time.time()
                
                success = self.vote_once_smart(driver)
                
                elapsed = time.time() - start_time
                
                if success:
                    self.success_count += 1
                    status = "SUCCESS"
                    # Longer delay after success to avoid detection
                    delay = random.randint(8, 15)
                else:
                    self.fail_count += 1
                    status = "FAILED"
                    # Even longer delay after failure
                    delay = random.randint(15, 30)
                
                # Print status
                print(f"[Worker {self.worker_id}] Vote #{self.vote_count:4d} | "
                      f"{status:7s} | Time: {elapsed:.1f}s | "
                      f"Success: {self.success_count:3d} | Fail: {self.fail_count:3d} | "
                      f"Blocked: {self.block_count:2d} | "
                      f"Next in {delay}s | {datetime.now().strftime('%H:%M:%S')}")
                
                # Smart delay between votes
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n[Worker {self.worker_id}] Stopped by user")
        finally:
            driver.quit()
            print(f"[Worker {self.worker_id}] Total votes: {self.vote_count}")
            print(f"[Worker {self.worker_id}] Successful: {self.success_count}")
            print(f"[Worker {self.worker_id}] Failed: {self.fail_count}")
            print(f"[Worker {self.worker_id}] Blocked: {self.block_count}")


if __name__ == "__main__":
    import sys
    
    worker_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    print("="*70)
    print(f"SMART CHROME VOTER - Worker {worker_id}")
    print("="*70)
    print("\nAnti-Detection Features:")
    print("  - Human-like random delays")
    print("  - Regular clicks (not JavaScript)")
    print("  - Random user agents")
    print("  - Webdriver property hidden")
    print("  - Smart retry after being blocked")
    print("\nThis will vote SLOWER but SAFER")
    print("~4-6 votes per minute per browser")
    print("\nPress Ctrl+C to stop")
    print("="*70)
    print()
    
    voter = SmartChromeVoter(worker_id)
    voter.run_infinite()
