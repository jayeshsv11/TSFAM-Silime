from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import argparse

class SeleniumAutoVoter:
    def __init__(self, headless=False):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.headless = headless
        
    def create_driver(self):
        """Create a new browser instance"""
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless')
        
        # Disable automation detection
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Random user agent
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        driver = webdriver.Chrome(options=chrome_options)
        
        # Execute script to hide webdriver property
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            '''
        })
        
        return driver
    
    def clear_browser_data(self, driver):
        """Clear cookies and storage"""
        print("Clearing browser data...")
        driver.delete_all_cookies()
        
        # Clear localStorage and sessionStorage
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        
    def vote_for_ashutosh(self):
        """Automated voting process"""
        driver = self.create_driver()
        
        try:
            print(f"Opening {self.url}...")
            driver.get(self.url)
            
            # Wait for page to load
            time.sleep(3)
            
            # Find all poll options
            print("Looking for Ashutosh Pratap Singh option...")
            
            # Try to find the radio button or label containing the name
            try:
                # Method 1: Find by label text
                labels = driver.find_elements(By.TAG_NAME, 'label')
                ashutosh_label = None
                
                for label in labels:
                    if 'Ashutosh Pratap Singh' in label.text:
                        ashutosh_label = label
                        print(f"Found option: {label.text}")
                        break
                
                if ashutosh_label:
                    # Click the label or associated radio button
                    ashutosh_label.click()
                    print("Clicked on Ashutosh Pratap Singh option")
                    time.sleep(1)
                    
                    # Find and click submit button
                    submit_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[type="submit"], input[type="submit"], .forminator-button-submit')
                    
                    if submit_buttons:
                        submit_buttons[0].click()
                        print("Clicked submit button")
                        time.sleep(3)
                        
                        # Check for success or error messages
                        page_source = driver.page_source
                        
                        if 'already voted' in page_source.lower():
                            print("\n⚠ Already voted - detected by website")
                            print("Possible reasons:")
                            print("  - IP address is tracked")
                            print("  - Browser fingerprint detected")
                            print("  - Server-side session tracking")
                            return False
                        elif 'success' in page_source.lower() or 'thank' in page_source.lower():
                            print("\n✓ Vote submitted successfully!")
                            return True
                        else:
                            print("\n? Vote status unclear")
                            print("Check the page manually")
                            
                            # Save screenshot for debugging
                            driver.save_screenshot('vote_result.png')
                            print("Screenshot saved: vote_result.png")
                            return None
                    else:
                        print("✗ Could not find submit button")
                        return False
                else:
                    print("✗ Could not find Ashutosh Pratap Singh option")
                    
                    # Print all available options for debugging
                    print("\nAvailable options:")
                    for idx, label in enumerate(labels):
                        if label.text.strip():
                            print(f"  {idx + 1}. {label.text.strip()}")
                    
                    return False
                    
            except Exception as e:
                print(f"✗ Error during voting: {str(e)}")
                driver.save_screenshot('error.png')
                print("Screenshot saved: error.png")
                return False
                
        finally:
            if not self.headless:
                input("\nPress Enter to close browser...")
            driver.quit()
    
    def vote_multiple_times(self, num_votes):
        """Attempt to vote multiple times (requires manual IP changes)"""
        print(f"Attempting to vote {num_votes} times...")
        print("Note: You'll need to change your IP address between votes\n")
        
        for i in range(num_votes):
            print(f"\n{'='*60}")
            print(f"Vote attempt {i + 1} of {num_votes}")
            print(f"{'='*60}")
            
            if i > 0:
                print("\nPlease change your IP address now:")
                print("  - Switch VPN server")
                print("  - Switch to mobile data/WiFi")
                print("  - Restart router")
                input("\nPress Enter when ready to continue...")
            
            result = self.vote_for_ashutosh()
            
            if result:
                print(f"✓ Vote {i + 1} successful")
            else:
                print(f"✗ Vote {i + 1} failed")
                
                retry = input("\nRetry this vote? (y/n): ")
                if retry.lower() == 'y':
                    continue
            
            time.sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Auto voter for Blizzard Production House')
    parser.add_argument('--votes', type=int, default=1, help='Number of times to vote')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Blizzard Production House - Selenium Auto Voter")
    print("Voting for: Ashutosh Pratap Singh")
    print("=" * 60)
    
    voter = SeleniumAutoVoter(headless=args.headless)
    
    if args.votes > 1:
        voter.vote_multiple_times(args.votes)
    else:
        voter.vote_for_ashutosh()
    
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)
