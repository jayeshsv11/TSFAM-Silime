from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class RealWorkingVoter:
    def __init__(self, headless=True):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.headless = headless
        
    def vote_once(self):
        """Vote using real browser interaction"""
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless=new')
        
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
            })
            
            print(f"Opening {self.url}...")
            driver.get(self.url)
            
            # Wait for page to load
            time.sleep(3)
            
            print("Looking for poll form...")
            
            # Wait for form to be present
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'form.forminator-poll, form[id*="forminator"]'))
                )
                print("✓ Form loaded")
            except:
                print("❌ Form not found")
                driver.save_screenshot('no_form.png')
                return False, "Form not found"
            
            # Find all clickable elements (labels or radio buttons)
            print("Searching for Ashutosh Pratap Singh option...")
            
            # Try to find by label text
            labels = driver.find_elements(By.TAG_NAME, 'label')
            found = False
            
            for label in labels:
                text = label.text.strip()
                print(f"  Checking: {text}")
                if 'ashutosh' in text.lower() and 'pratap' in text.lower() and 'singh' in text.lower():
                    print(f"✓ Found: {text}")
                    label.click()
                    found = True
                    time.sleep(1)
                    break
            
            if not found:
                # Try radio buttons directly
                radios = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
                for radio in radios:
                    value = radio.get_attribute('value') or ''
                    if 'ashutosh' in value.lower():
                        print(f"✓ Found radio: {value}")
                        driver.execute_script("arguments[0].click();", radio)
                        found = True
                        time.sleep(1)
                        break
            
            if not found:
                print("❌ Could not find Ashutosh Pratap Singh option")
                # Print all available options for debugging
                print("\nAvailable options:")
                for idx, label in enumerate(labels):
                    if label.text.strip():
                        print(f"  {idx+1}. {label.text.strip()}")
                
                driver.save_screenshot('options_not_found.png')
                return False, "Option not found"
            
            # Find and click submit button
            print("Looking for submit button...")
            submit_buttons = driver.find_elements(By.CSS_SELECTOR, 
                'button[type="submit"], input[type="submit"], .forminator-button-submit, button.forminator-button')
            
            if submit_buttons:
                print(f"✓ Found submit button")
                submit_buttons[0].click()
                print("Clicked submit!")
                time.sleep(4)
                
                # Check result
                page_source = driver.page_source.lower()
                
                if 'thank' in page_source or 'success' in page_source:
                    print("\n✓✓✓ VOTE SUCCESSFUL! ✓✓✓")
                    driver.save_screenshot('success.png')
                    return True, "Success"
                elif 'already' in page_source and 'voted' in page_source:
                    print("\n⚠ Already voted (IP detected)")
                    driver.save_screenshot('already_voted.png')
                    return False, "Already voted"
                else:
                    print("\n? Vote status unclear - checking page...")
                    driver.save_screenshot('result.png')
                    
                    # Try to find result message
                    try:
                        result_msg = driver.find_element(By.CSS_SELECTOR, '.forminator-response-message, .forminator-error, .forminator-success')
                        msg_text = result_msg.text
                        print(f"Result message: {msg_text}")
                        return 'success' in msg_text.lower() or 'thank' in msg_text.lower(), msg_text
                    except:
                        print("Could not find result message")
                        return None, "Status unclear"
            else:
                print("❌ Submit button not found")
                driver.save_screenshot('no_submit.png')
                return False, "No submit button"
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            driver.save_screenshot('error.png')
            return False, str(e)
        finally:
            driver.quit()


if __name__ == "__main__":
    print("="*70)
    print("REAL WORKING VOTER - Using Selenium with actual browser")
    print("Voting for: Ashutosh Pratap Singh")
    print("="*70)
    print()
    
    voter = RealWorkingVoter(headless=False)  # Set to True to hide browser
    
    success, message = voter.vote_once()
    
    print("\n" + "="*70)
    if success:
        print("✓ VOTE WAS SUCCESSFUL!")
        print("Check the website to verify the vote count increased.")
    elif success == False:
        print(f"✗ VOTE FAILED: {message}")
    else:
        print(f"? UNCLEAR: {message}")
        print("Check screenshots for details.")
    print("="*70)
