"""
FAST FRESH BROWSER VOTER - Optimized for speed
Closes and reopens browser but MUCH faster
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime

class FastFreshVoter:
    def __init__(self, worker_id):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.worker_id = worker_id
        self.vote_count = 0
        self.success_count = 0
        self.fail_count = 0
        
    def create_driver(self):
        """Create Chrome browser - FAST"""
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        options.page_load_strategy = 'eager'  # Don't wait for all resources - FAST!
        
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver
    
    def vote_once_fast(self):
        """Single vote - OPTIMIZED FOR SPEED"""
        driver = None
        try:
            # Create browser - NO delay
            driver = self.create_driver()
            
            # Load page
            driver.get(self.url)
            
            # Wait for form - SHORT timeout
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'form'))
                )
            except:
                return False
            
            # Wait for labels - REDUCED
            time.sleep(1.5)
            
            # Find and click option - FAST
            labels = driver.find_elements(By.TAG_NAME, 'label')
            if len(labels) == 0:
                return False
            
            for label in labels:
                try:
                    text = label.text.lower()
                    if 'ashutosh' in text and 'pratap' in text:
                        # NO delay, just click
                        driver.execute_script("arguments[0].click();", label)
                        break
                except:
                    continue
            
            # Minimal delay
            time.sleep(0.3)
            
            # Submit - FAST
            try:
                submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
            except:
                submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            
            driver.execute_script("arguments[0].click();", submit)
            
            # Wait for response - REDUCED
            time.sleep(2)
            
            # Quick check
            if 'tech' not in driver.current_url.lower():
                return False
            
            page_source = driver.page_source.lower()
            return 'thank' in page_source or 'success' in page_source
            
        except:
            return False
        finally:
            # Close browser immediately
            if driver:
                driver.quit()
    
    def run_infinite(self):
        """Keep voting with fresh browser - FAST"""
        print(f"[Worker {self.worker_id}] FAST FRESH BROWSER voter starting...")
        print(f"[Worker {self.worker_id}] Target: 5-8 votes/min per browser")
        print()
        
        try:
            while True:
                self.vote_count += 1
                start_time = time.time()
                
                success = self.vote_once_fast()
                elapsed = time.time() - start_time
                
                if success:
                    self.success_count += 1
                    print(f"[Worker {self.worker_id}] Vote #{self.vote_count:3d} | SUCCESS | {elapsed:.1f}s | Total: {self.success_count}✓ {self.fail_count}✗")
                    delay = 2  # Very short delay after success
                else:
                    self.fail_count += 1
                    print(f"[Worker {self.worker_id}] Vote #{self.vote_count:3d} | FAILED  | {elapsed:.1f}s | Total: {self.success_count}✓ {self.fail_count}✗")
                    delay = 5  # Longer delay after failure
                
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n[Worker {self.worker_id}] Stopped")
        finally:
            rate = (self.success_count / (time.time() - start_time) * 60) if self.vote_count > 0 else 0
            print(f"\n[Worker {self.worker_id}] Final: {self.success_count}/{self.vote_count} ({rate:.1f} votes/min)")


if __name__ == "__main__":
    import sys
    
    worker_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    print("="*70)
    print(f"FAST FRESH BROWSER VOTER - Worker {worker_id}")
    print("="*70)
    print("\nOptimizations:")
    print("  - Minimal delays (2-5 seconds between votes)")
    print("  - Fast page loading (eager strategy)")
    print("  - JavaScript clicks (faster)")
    print("  - Browser closes after each vote")
    print("\nTarget: 5-8 votes per minute")
    print("="*70)
    print()
    
    voter = FastFreshVoter(worker_id)
    voter.run_infinite()
