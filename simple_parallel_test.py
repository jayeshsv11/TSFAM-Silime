"""
SIMPLE PARALLEL VOTER - No IP rotation needed
Just runs 5 browsers in parallel and votes
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from concurrent.futures import ThreadPoolExecutor
import threading

class SimpleParallelVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.lock = threading.Lock()
        self.successful = 0
        self.failed = 0
        
    def vote_once(self, worker_id):
        """Single vote attempt"""
        options = Options()
        # Comment out headless to SEE the browsers working
        # options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=options)
        
        try:
            print(f"[Worker {worker_id}] Opening browser...")
            driver.get(self.url)
            
            # Wait for page to load completely
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'form'))
            )
            time.sleep(2)  # Extra wait for JS
            
            print(f"[Worker {worker_id}] Finding option...")
            # Find and click Ashutosh option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            clicked = False
            
            for label in labels:
                try:
                    text = label.text.lower()
                    if 'ashutosh' in text and 'pratap' in text:
                        print(f"[Worker {worker_id}] Found option, clicking...")
                        label.click()
                        clicked = True
                        break
                except:
                    continue
            
            if not clicked:
                print(f"[Worker {worker_id}] X Option not found!")
                return False
            
            time.sleep(1)
            
            # Click submit button
            print(f"[Worker {worker_id}] Submitting vote...")
            try:
                submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            except:
                # Try alternative selectors
                try:
                    submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
                except:
                    submit = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit') or contains(text(), 'Vote')]")
            
            submit.click()
            
            time.sleep(3)  # Wait for response
            
            # Check if successful
            page_source = driver.page_source.lower()
            if 'thank' in page_source or 'success' in page_source:
                with self.lock:
                    self.successful += 1
                print(f"[Worker {worker_id}] SUCCESS!")
                return True
            elif 'already' in page_source or 'voted' in page_source:
                with self.lock:
                    self.failed += 1
                print(f"[Worker {worker_id}] X Already voted from this IP")
                return False
            else:
                with self.lock:
                    self.failed += 1
                print(f"[Worker {worker_id}] X Unknown response")
                return False
                
        except Exception as e:
            with self.lock:
                self.failed += 1
            print(f"[Worker {worker_id}] X Error: {str(e)[:50]}")
            return False
        finally:
            time.sleep(2)  # Keep browser open a bit to see result
            driver.quit()
            print(f"[Worker {worker_id}] Browser closed")
    
    def vote_parallel(self, num_workers=5):
        """Run multiple browsers in parallel"""
        print("="*70)
        print("SIMPLE PARALLEL VOTER")
        print("="*70)
        print(f"\nStarting {num_workers} browsers in parallel...")
        print("You will SEE the browsers opening and voting!\n")
        print("="*70)
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(self.vote_once, i+1) for i in range(num_workers)]
            # Wait for all to complete
            for future in futures:
                future.result()
        
        elapsed = time.time() - start_time
        
        print("\n" + "="*70)
        print("RESULTS")
        print("="*70)
        print(f"Total browsers: {num_workers}")
        print(f"Successful: {self.successful}")
        print(f"Failed: {self.failed}")
        print(f"Time taken: {elapsed:.1f} seconds")
        print("="*70)
        
        if self.successful == 1 and self.failed == num_workers - 1:
            print("\nIMPORTANT:")
            print("Only 1 vote succeeded - this is expected!")
            print("All votes are from the SAME IP address.")
            print("Website only counts 1 vote per IP.")
            print("\nTo get MORE votes counted:")
            print("- Toggle airplane mode and run again")
            print("- Or use VPN and run again")
            print("="*70)


if __name__ == "__main__":
    print("\n" + "="*70)
    print("SIMPLE TEST - 5 Parallel Browsers")
    print("="*70)
    print("\nThis will:")
    print("1. Open 5 Chrome browsers (you will see them!)")
    print("2. Each browser votes")
    print("3. Shows you exactly what's happening")
    print("\nExpected result:")
    print("- 1 vote will succeed")
    print("- 4 votes will fail (same IP)")
    print("\n" + "="*70)
    
    input("\nPress Enter to start...")
    
    voter = SimpleParallelVoter()
    voter.vote_parallel(num_workers=5)
    
    print("\n")
    input("Press Enter to exit...")
