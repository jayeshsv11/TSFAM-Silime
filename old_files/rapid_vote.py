from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def vote_once(headless=True):
    """Vote once quickly"""
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument('--headless')
    
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
        
        driver.get("https://blizzardproductionhouse.com/tech/")
        time.sleep(2)
        
        # Clear all storage
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        
        # Reload page
        driver.refresh()
        time.sleep(2)
        
        # Find and click Ashutosh option
        labels = driver.find_elements(By.TAG_NAME, 'label')
        
        for label in labels:
            if 'Ashutosh Pratap Singh' in label.text:
                label.click()
                time.sleep(0.5)
                break
        
        # Submit
        submit_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[type="submit"], input[type="submit"], .forminator-button-submit')
        if submit_buttons:
            submit_buttons[0].click()
            time.sleep(2)
            
            page_source = driver.page_source
            
            if 'already voted' in page_source.lower():
                return False, "Already voted (IP restriction detected)"
            elif 'success' in page_source.lower() or 'thank' in page_source.lower():
                return True, "Success"
            else:
                return None, "Status unclear"
        
        return False, "Submit button not found"
        
    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        driver.quit()

if __name__ == "__main__":
    print("=" * 60)
    print("RAPID VOTING - Ashutosh Pratap Singh")
    print("=" * 60)
    
    votes = 10  # Number of attempts
    successful = 0
    failed = 0
    
    for i in range(1, votes + 1):
        print(f"\n[{i}/{votes}] Voting...", end=" ")
        
        success, msg = vote_once(headless=True)
        
        if success:
            successful += 1
            print(f"✓ {msg}")
        elif success == False and "IP restriction" in msg:
            failed += 1
            print(f"✗ {msg}")
            print("\n" + "=" * 60)
            print("IP RESTRICTION DETECTED!")
            print(f"Successful votes: {successful}")
            print(f"Failed votes: {failed}")
            print("=" * 60)
            print("\nNeed to change method - IP address is being tracked.")
            print("Options:")
            print("1. Use VPN and change servers between votes")
            print("2. Use proxy rotation")
            print("3. Use different devices/networks")
            break
        else:
            failed += 1
            print(f"? {msg}")
    
    else:
        print("\n" + "=" * 60)
        print(f"COMPLETE - Attempted {votes} votes")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print("=" * 60)
