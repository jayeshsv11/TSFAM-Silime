from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

class FastSeleniumVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.lock = threading.Lock()
        
    def create_driver(self):
        """Create a headless Chrome instance"""
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
        })
        
        return driver
    
    def vote_once(self, vote_num):
        """Single vote attempt"""
        driver = self.create_driver()
        
        try:
            driver.get(self.url)
            time.sleep(2)
            
            # Wait for form
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'form.forminator-poll, form[id*="forminator"]'))
            )
            
            # Find and click Ashutosh option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            found = False
            
            for label in labels:
                if 'ashutosh' in label.text.lower() and 'pratap' in label.text.lower():
                    label.click()
                    found = True
                    break
            
            if not found:
                return vote_num, False, "Option not found"
            
            time.sleep(0.5)
            
            # Click submit
            submit_buttons = driver.find_elements(By.CSS_SELECTOR, 
                'button[type="submit"], input[type="submit"], .forminator-button-submit')
            
            if submit_buttons:
                submit_buttons[0].click()
                time.sleep(3)
                
                page_source = driver.page_source.lower()
                
                if 'thank' in page_source or 'success' in page_source:
                    return vote_num, True, "Success"
                elif 'already' in page_source:
                    return vote_num, False, "Already voted"
                else:
                    return vote_num, None, "Unclear"
            else:
                return vote_num, False, "No submit button"
                
        except Exception as e:
            return vote_num, False, str(e)[:50]
        finally:
            driver.quit()
    
    def vote_parallel(self, total_votes, max_workers=5):
        """Vote using multiple browser instances in parallel"""
        print(f"Starting {total_votes} votes with {max_workers} parallel browsers...\n")
        
        successful = 0
        failed = 0
        unclear = 0
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.vote_once, i+1): i+1 for i in range(total_votes)}
            
            for future in as_completed(futures):
                vote_num, success, message = future.result()
                
                with self.lock:
                    if success:
                        successful += 1
                        print(f"[{vote_num}/{total_votes}] ✓ Success")
                    elif success == False:
                        failed += 1
                        print(f"[{vote_num}/{total_votes}] ✗ Failed: {message}")
                    else:
                        unclear += 1
                        print(f"[{vote_num}/{total_votes}] ? Unclear: {message}")
        
        elapsed = time.time() - start_time
        
        print("\n" + "="*70)
        print("RESULTS")
        print("="*70)
        print(f"Total votes attempted: {total_votes}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Unclear: {unclear}")
        print(f"Time taken: {elapsed:.1f} seconds")
        print(f"Rate: {total_votes/elapsed:.1f} votes/second")
        print("="*70)
        
        return successful, failed, unclear


if __name__ == "__main__":
    print("="*70)
    print("FAST SELENIUM VOTER - Multiple parallel browsers")
    print("Voting for: Ashutosh Pratap Singh")
    print("="*70)
    print()
    print("IMPORTANT: This uses REAL browser automation")
    print("Each vote opens a new browser instance")
    print("Recommended: 5-10 parallel browsers max")
    print()
    
    try:
        total = int(input("How many votes? (1-100): "))
        workers = int(input("Parallel browsers? (1-10, recommended 5): "))
        
        if total < 1 or total > 100:
            print("Please enter 1-100 votes")
            exit()
        
        if workers < 1 or workers > 10:
            print("Please enter 1-10 workers")
            exit()
        
        print()
        voter = FastSeleniumVoter()
        voter.vote_parallel(total, workers)
        
    except ValueError:
        print("Invalid input!")
    except KeyboardInterrupt:
        print("\n\nStopped by user")
