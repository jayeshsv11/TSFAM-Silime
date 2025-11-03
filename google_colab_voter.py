"""
GOOGLE COLAB VOTER - Run on Google's servers (FREE!)

Instructions:
1. Go to https://colab.research.google.com
2. Create new notebook
3. Copy this entire file into a code cell
4. Click Run
5. Close browser - it keeps running!
"""

# Step 1: Install dependencies
print("Installing Chrome and dependencies...")
!apt-get update > /dev/null 2>&1
!apt install chromium-chromedriver > /dev/null 2>&1
!pip install selenium > /dev/null 2>&1

print("✓ Installation complete!")
print()

# Step 2: Import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime
from threading import Thread

class ColabVoter:
    def __init__(self, worker_id):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.worker_id = worker_id
        self.vote_count = 0
        self.success_count = 0
        self.fail_count = 0
        
    def create_driver(self):
        """Create Chrome browser for Colab"""
        options = Options()
        options.add_argument('--headless')  # Must be headless on Colab
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver
    
    def vote_once_fresh(self):
        """Vote with fresh browser"""
        driver = None
        try:
            # Create fresh browser
            driver = self.create_driver()
            time.sleep(random.uniform(1, 2))
            
            # Load page
            driver.get(self.url)
            time.sleep(random.uniform(2, 4))
            
            # Check redirect
            if 'tech' not in driver.current_url.lower():
                return False
            
            # Wait for form
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'form'))
            )
            time.sleep(2)
            
            # Find option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            if len(labels) == 0:
                return False
            
            found = False
            for label in labels:
                try:
                    text = label.text.lower()
                    if 'ashutosh' in text and 'pratap' in text:
                        time.sleep(random.uniform(0.5, 1.5))
                        label.click()
                        found = True
                        break
                except:
                    continue
            
            if not found:
                return False
            
            time.sleep(random.uniform(0.5, 1.5))
            
            # Submit
            try:
                submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
            except:
                submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            
            time.sleep(random.uniform(0.3, 0.7))
            submit.click()
            time.sleep(3)
            
            # Check result
            if 'tech' not in driver.current_url.lower():
                return False
            
            page_source = driver.page_source.lower()
            return 'thank' in page_source or 'success' in page_source
            
        except Exception as e:
            print(f"[Worker {self.worker_id}] Error: {str(e)[:50]}")
            return False
        finally:
            if driver:
                driver.quit()
                time.sleep(1)
    
    def run_infinite(self, max_votes=None):
        """Keep voting"""
        print(f"[Worker {self.worker_id}] Starting voting on Google Colab...")
        print(f"[Worker {self.worker_id}] Running in cloud - no laptop load!")
        print()
        
        try:
            while True:
                if max_votes and self.vote_count >= max_votes:
                    print(f"[Worker {self.worker_id}] Reached max votes: {max_votes}")
                    break
                
                self.vote_count += 1
                start_time = time.time()
                
                print(f"\n[Worker {self.worker_id}] Vote #{self.vote_count}")
                
                success = self.vote_once_fresh()
                elapsed = time.time() - start_time
                
                if success:
                    self.success_count += 1
                    print(f"[Worker {self.worker_id}] SUCCESS! ({elapsed:.1f}s)")
                    delay = random.randint(5, 10)
                else:
                    self.fail_count += 1
                    print(f"[Worker {self.worker_id}] Failed ({elapsed:.1f}s)")
                    delay = random.randint(10, 20)
                
                print(f"[Worker {self.worker_id}] Stats: {self.success_count}✓ {self.fail_count}✗")
                print(f"[Worker {self.worker_id}] Next in {delay}s...")
                
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n[Worker {self.worker_id}] Stopped")
        finally:
            print(f"\n[Worker {self.worker_id}] Final: {self.success_count}/{self.vote_count}")

# Step 3: Configuration
NUM_BROWSERS = 5  # Change this (1-10)
VOTES_PER_BROWSER = None  # None = infinite, or set number like 50

print("="*70)
print("GOOGLE COLAB VOTER - Running on Cloud")
print("="*70)
print(f"\nConfiguration:")
print(f"  Browsers: {NUM_BROWSERS}")
print(f"  Votes per browser: {'Infinite' if VOTES_PER_BROWSER is None else VOTES_PER_BROWSER}")
print(f"  No laptop load - runs on Google servers!")
print()
print("="*70)
print("\nStarting in 3 seconds...")
print("="*70)
time.sleep(3)

# Step 4: Start voting threads
threads = []
for i in range(NUM_BROWSERS):
    voter = ColabVoter(i+1)
    thread = Thread(target=voter.run_infinite, args=(VOTES_PER_BROWSER,))
    thread.start()
    threads.append(thread)
    time.sleep(2)  # Stagger starts

# Wait for all threads
for thread in threads:
    thread.join()

print("\n" + "="*70)
print("ALL VOTERS FINISHED")
print("="*70)
