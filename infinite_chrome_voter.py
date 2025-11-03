"""
INFINITE CHROME VOTER - Continuous Voting
Uses Chrome browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

class InfiniteChromeVoter:
    def __init__(self, worker_id):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.worker_id = worker_id
        self.vote_count = 0
        self.success_count = 0
        self.fail_count = 0
        
    def create_driver(self):
        """Create Chrome browser instance"""
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        options.page_load_strategy = 'eager'  # Don't wait for all resources
        
        # Uncomment to hide browser window
        # options.add_argument('--headless=new')
        
        return webdriver.Chrome(options=options)
    
    def vote_once_fast(self, driver):
        """Single vote - OPTIMIZED FOR SPEED"""
        try:
            # Load page
            driver.get(self.url)
            
            # Check if redirected to homepage
            time.sleep(1)
            current_url = driver.current_url
            if 'tech' not in current_url.lower():
                print(f"[Worker {self.worker_id}] BLOCKED - Redirected to homepage. Waiting 30 seconds...")
                time.sleep(30)  # Wait before retry
                driver.get(self.url)
                time.sleep(2)
            
            # Wait for form (max 10 seconds)
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'form'))
                )
            except:
                print(f"[Worker {self.worker_id}] No form found - likely blocked")
                return False
            
            # Wait for labels to load (IMPORTANT!)
            time.sleep(2)
            
            # Find and click option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            if len(labels) == 0:
                print(f"[Worker {self.worker_id}] No labels found - page issue")
                return False
                
            for label in labels:
                try:
                    text = label.text.lower()
                    if 'ashutosh' in text and 'pratap' in text:
                        time.sleep(0.3)
                        driver.execute_script("arguments[0].click();", label)
                        break
                except:
                    continue
            
            # Wait before submit
            time.sleep(0.5)
            
            # Find and click submit
            try:
                submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
            except:
                try:
                    submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
                except:
                    try:
                        submit = driver.find_element(By.XPATH, "//button")
                    except:
                        print(f"[Worker {self.worker_id}] No submit button - page issue")
                        return False
            
            driver.execute_script("arguments[0].click();", submit)
            
            # Wait for response (IMPORTANT!)
            time.sleep(3)
            
            # Check if redirected after submit
            current_url = driver.current_url
            if 'tech' not in current_url.lower():
                print(f"[Worker {self.worker_id}] BLOCKED after submit - Website detected bot")
                return False
            
            # Quick check
            page_source = driver.page_source.lower()
            success = 'thank' in page_source or 'success' in page_source
            
            return success
            
        except Exception as e:
            print(f"[Worker {self.worker_id}] Error: {str(e)[:50]}")
            return False
    
    def run_infinite(self):
        """Keep voting forever until stopped"""
        print(f"[Worker {self.worker_id}] Starting infinite voting...")
        print(f"[Worker {self.worker_id}] Press Ctrl+C to stop")
        
        driver = self.create_driver()
        
        try:
            while True:
                self.vote_count += 1
                start_time = time.time()
                
                success = self.vote_once_fast(driver)
                
                elapsed = time.time() - start_time
                
                if success:
                    self.success_count += 1
                    status = "SUCCESS"
                else:
                    self.fail_count += 1
                    status = "FAILED"
                
                # Print status
                print(f"[Worker {self.worker_id}] Vote #{self.vote_count:4d} | "
                      f"{status:7s} | Time: {elapsed:.1f}s | "
                      f"Success: {self.success_count:3d} | Fail: {self.fail_count:3d} | "
                      f"{datetime.now().strftime('%H:%M:%S')}")
                
                # Add delay to avoid bot detection (IMPORTANT!)
                if success:
                    time.sleep(5)  # Wait 5 seconds between successful votes
                else:
                    time.sleep(10)  # Wait longer after failure
                
        except KeyboardInterrupt:
            print(f"\n[Worker {self.worker_id}] Stopped by user")
        finally:
            driver.quit()
            print(f"[Worker {self.worker_id}] Total votes: {self.vote_count}")
            print(f"[Worker {self.worker_id}] Successful: {self.success_count}")
            print(f"[Worker {self.worker_id}] Failed: {self.fail_count}")


if __name__ == "__main__":
    import sys
    
    # Get worker ID from command line (default 1)
    worker_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    print("="*70)
    print(f"INFINITE CHROME VOTER - Worker {worker_id}")
    print("="*70)
    print("\nThis will vote CONTINUOUSLY until you stop it")
    print("Press Ctrl+C to stop")
    print("\nUsing Chrome Browser")
    print("="*70)
    print()
    
    voter = InfiniteChromeVoter(worker_id)
    voter.run_infinite()
