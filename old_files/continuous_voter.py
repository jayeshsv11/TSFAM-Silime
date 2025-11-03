"""
CONTINUOUS VOTER - Keeps voting forever until you stop it
Runs in loop, optimized for speed
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

class ContinuousVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.total_successful = 0
        self.total_failed = 0
        self.total_attempts = 0
        
    def vote_once_optimized(self):
        """Super optimized single vote"""
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
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
            })
            
            driver.set_page_load_timeout(10)
            driver.get(self.url)
            time.sleep(3)  # Wait for page to load
            
            # Find and click Ashutosh option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            found = False
            for label in labels:
                if 'ashutosh' in label.text.lower() and 'pratap' in label.text.lower() and 'singh' in label.text.lower():
                    label.click()
                    found = True
                    time.sleep(0.5)
                    break
            
            if not found:
                return False
            
            # Submit
            submit_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[type="submit"], input[type="submit"], .forminator-button-submit')
            if submit_buttons:
                submit_buttons[0].click()
                time.sleep(3)
                
                success = 'thank' in driver.page_source.lower() or 'success' in driver.page_source.lower()
                return success
            else:
                return False
                
        except Exception as e:
            return False
        finally:
            driver.quit()
    
    def run_continuous(self, delay_between_votes=0):
        """Keep voting forever"""
        print("="*70)
        print("CONTINUOUS VOTER - Running until you press Ctrl+C")
        print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
        print("="*70)
        print()
        
        try:
            while True:
                self.total_attempts += 1
                
                start = time.time()
                success = self.vote_once_optimized()
                elapsed = time.time() - start
                
                if success:
                    self.total_successful += 1
                    print(f"[{self.total_attempts}] ✓ SUCCESS | Time: {elapsed:.1f}s | Total Success: {self.total_successful}")
                else:
                    self.total_failed += 1
                    print(f"[{self.total_attempts}] ✗ FAILED | Time: {elapsed:.1f}s | Total Failed: {self.total_failed}")
                
                if delay_between_votes > 0:
                    time.sleep(delay_between_votes)
                    
        except KeyboardInterrupt:
            print("\n" + "="*70)
            print("STOPPED BY USER")
            print("="*70)
            print(f"Total attempts: {self.total_attempts}")
            print(f"Successful: {self.total_successful}")
            print(f"Failed: {self.total_failed}")
            print(f"Success rate: {(self.total_successful/self.total_attempts*100):.1f}%")
            print("="*70)


if __name__ == "__main__":
    print("\nCONTINUOUS VOTER")
    print("This will keep voting until you press Ctrl+C\n")
    
    delay = input("Delay between votes (seconds, 0 for none): ").strip()
    delay = float(delay) if delay else 0
    
    print(f"\nStarting continuous voting (delay: {delay}s)...")
    print("Press Ctrl+C to stop\n")
    
    voter = ContinuousVoter()
    voter.run_continuous(delay_between_votes=delay)
