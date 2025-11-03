"""
SINGLE VOTE TEST - Chrome Version
Tests 1 vote with detailed output using Chrome
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("="*70)
print("SINGLE VOTE TEST - Chrome Browser")
print("="*70)
print("\nTesting 1 vote with detailed output...")
print()

# Create Chrome browser
print("[1/6] Creating Chrome browser...")
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
print("      Browser created!")

try:
    # Load page
    print("[2/6] Loading page...")
    driver.get("https://blizzardproductionhouse.com/tech/")
    
    # Wait for form
    print("[3/6] Waiting for form to load...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'form'))
    )
    print("      Form found! Waiting for labels to load...")
    time.sleep(3)  # Extra time for labels to appear
    
    # Find option
    print("[4/6] Finding Ashutosh Pratap Singh option...")
    labels = driver.find_elements(By.TAG_NAME, 'label')
    print(f"      Found {len(labels)} labels total")
    
    # Print all labels for debugging
    for i, label in enumerate(labels[:10]):  # Show first 10
        try:
            print(f"      Label {i+1}: {label.text[:50]}")
        except:
            pass
    
    found = False
    
    print("      Searching for Ashutosh Pratap Singh...")
    for label in labels:
        try:
            text = label.text.lower()
            if 'ashutosh' in text and 'pratap' in text:
                print(f"      MATCH FOUND: {label.text}")
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", label)
                found = True
                break
        except:
            continue
    
    if not found:
        print("      ERROR: Option not found!")
        driver.quit()
        exit(1)
    
    time.sleep(1)
    
    # Submit
    print("[5/6] Submitting vote...")
    print("      Looking for submit button...")
    try:
        submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
        print("      Found submit button (class=forminator-button-submit)")
    except:
        try:
            submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            print("      Found submit button (type=submit)")
        except:
            submit = driver.find_element(By.XPATH, "//button")
            print("      Found submit button (xpath)")
    
    print("      Clicking submit...")
    driver.execute_script("arguments[0].click();", submit)
    print("      Waiting for response...")
    time.sleep(3)  # Wait longer for response
    
    # Check result
    print("[6/6] Checking result...")
    page_source = driver.page_source.lower()
    
    if 'thank' in page_source or 'success' in page_source:
        print("\n" + "="*70)
        print("SUCCESS! Vote was counted!")
        print("="*70)
    elif 'already' in page_source or 'voted' in page_source:
        print("\n" + "="*70)
        print("ALREADY VOTED - Same IP already voted")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("UNKNOWN RESPONSE - Check browser window")
        print("="*70)
        print("\nPage source snippet:")
        print(page_source[page_source.find('forminator'):page_source.find('forminator')+500] if 'forminator' in page_source else page_source[:500])
    
    print("\nBrowser will stay open for 5 seconds so you can see...")
    time.sleep(5)
    
except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\nBrowser closed.")
    print("\nTest complete!")
