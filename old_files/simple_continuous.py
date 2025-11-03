"""
SIMPLE CONTINUOUS VOTER - Just runs and works
No complex options, just votes continuously
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

def vote_once():
    """Single vote - simple and reliable"""
    options = Options()
    # options.add_argument('--headless=new')  # REMOVED - headless causes issues
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('--start-minimized')  # Minimize instead of headless
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
        })
        
        driver.get("https://blizzardproductionhouse.com/tech/")
        time.sleep(3)
        
        # Find Ashutosh option
        labels = driver.find_elements(By.TAG_NAME, 'label')
        for label in labels:
            if 'ashutosh' in label.text.lower() and 'pratap' in label.text.lower():
                label.click()
                time.sleep(0.5)
                break
        
        # Submit
        submit = driver.find_elements(By.CSS_SELECTOR, 'button[type="submit"]')
        if submit:
            submit[0].click()
            time.sleep(3)
            return 'thank' in driver.page_source.lower() or 'success' in driver.page_source.lower()
        return False
        
    except:
        return False
    finally:
        driver.quit()

# Main loop
print("="*70)
print("CONTINUOUS VOTER - Ashutosh Pratap Singh")
print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
print("Press Ctrl+C to stop")
print("="*70)
print()

success_count = 0
fail_count = 0
total = 0

try:
    while True:
        total += 1
        start = time.time()
        
        if vote_once():
            success_count += 1
            elapsed = time.time() - start
            print(f"[{total}] ✓ SUCCESS ({elapsed:.1f}s) | Total: {success_count}")
        else:
            fail_count += 1
            elapsed = time.time() - start
            print(f"[{total}] ✗ FAILED ({elapsed:.1f}s) | Failed: {fail_count}")
            
except KeyboardInterrupt:
    print("\n" + "="*70)
    print("STOPPED")
    print("="*70)
    print(f"Total: {total} | Success: {success_count} | Failed: {fail_count}")
    print("="*70)
