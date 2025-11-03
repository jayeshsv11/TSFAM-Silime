"""
OPTIMIZED FRESH BROWSER VOTER
Waits for success, then immediately reopens browser
No extra delays
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

class OptimizedFreshVoter:
    def __init__(self, worker_id):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.worker_id = worker_id
        self.vote_count = 0
        self.success_count = 0
        self.fail_count = 0
        
    def create_driver(self):
        """Create Chrome browser"""
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver
    
    def vote_once_optimized(self):
        """Single vote - wait for success then close immediately"""
        driver = None
        try:
            print(f"[Worker {self.worker_id}] Opening browser...")
            
            # Create browser
            driver = self.create_driver()
            
            # Load page
            print(f"[Worker {self.worker_id}] Loading page...")
            driver.get(self.url)
            
            # Wait for form
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'form'))
                )
            except:
                print(f"[Worker {self.worker_id}] No form found")
                return False
            
            # Wait for labels to load
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
                        time.sleep(0.5)
                        label.click()
                        found = True
                        break
                except:
                    continue
            
            if not found:
                print(f"[Worker {self.worker_id}] Option not found")
                return False
            
            time.sleep(0.5)
            
            # Submit
            print(f"[Worker {self.worker_id}] Submitting...")
            try:
                submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
            except:
                submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            
            submit.click()
            
            # Wait for success response
            print(f"[Worker {self.worker_id}] Waiting for response...")
            time.sleep(3)
            
            # Check if redirected
            if 'tech' not in driver.current_url.lower():
                print(f"[Worker {self.worker_id}] BLOCKED - Redirected")
                return False
            
            # Check result
            page_source = driver.page_source.lower()
            if 'thank' in page_source or 'success' in page_source:
                print(f"[Worker {self.worker_id}] SUCCESS!")
                return True
            else:
                print(f"[Worker {self.worker_id}] Failed - no success message")
                return False
            
        except Exception as e:
            print(f"[Worker {self.worker_id}] Error: {str(e)[:50]}")
            return False
            
        finally:
            # Close browser IMMEDIATELY after checking response
            if driver:
                print(f"[Worker {self.worker_id}] Closing browser...")
                driver.quit()
                # NO EXTRA DELAY HERE - immediately ready for next vote
    
    def run_infinite(self):
        """Keep voting - no delays between votes"""
        print(f"[Worker {self.worker_id}] Starting optimized voting...")
        print(f"[Worker {self.worker_id}] No delays between votes")
        print()
        
        try:
            while True:
                self.vote_count += 1
                start_time = time.time()
                
                print(f"\n[Worker {self.worker_id}] ===== VOTE #{self.vote_count} =====")
                
                success = self.vote_once_optimized()
                
                elapsed = time.time() - start_time
                
                if success:
                    self.success_count += 1
                else:
                    self.fail_count += 1
                
                print(f"[Worker {self.worker_id}] Time: {elapsed:.1f}s | Total: {self.success_count}✓ {self.fail_count}✗")
                print(f"[Worker {self.worker_id}] {datetime.now().strftime('%H:%M:%S')}")
                
                # NO DELAY - immediately start next vote
                
        except KeyboardInterrupt:
            print(f"\n\n[Worker {self.worker_id}] Stopped by user")
        finally:
            print(f"\n[Worker {self.worker_id}] ===== FINAL STATS =====")
            print(f"[Worker {self.worker_id}] Total: {self.vote_count}")
            print(f"[Worker {self.worker_id}] Success: {self.success_count}")
            print(f"[Worker {self.worker_id}] Failed: {self.fail_count}")


if __name__ == "__main__":
    import sys
    
    worker_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    print("="*70)
    print(f"OPTIMIZED FRESH BROWSER VOTER - Worker {worker_id}")
    print("="*70)
    print("\nHow it works:")
    print("  1. Opens browser")
    print("  2. Votes")
    print("  3. Waits for success response")
    print("  4. Closes browser IMMEDIATELY")
    print("  5. Opens new browser IMMEDIATELY")
    print("  6. Repeat - NO delays")
    print("\nFast but accurate!")
    print("="*70)
    print()
    
    voter = OptimizedFreshVoter(worker_id)
    voter.run_infinite()
