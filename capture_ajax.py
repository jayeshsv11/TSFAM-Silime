"""
Simpler analysis - capture the AJAX POST request
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

print("="*70)
print("CAPTURING AJAX VOTE REQUEST")
print("="*70)

driver.get("https://blizzardproductionhouse.com/tech/")
time.sleep(3)

# Inject script to capture XHR/Fetch
driver.execute_script("""
    window.capturedRequests = [];
    
    // Intercept XMLHttpRequest
    const originalXHROpen = XMLHttpRequest.prototype.open;
    const originalXHRSend = XMLHttpRequest.prototype.send;
    
    XMLHttpRequest.prototype.open = function(method, url) {
        this._method = method;
        this._url = url;
        return originalXHROpen.apply(this, arguments);
    };
    
    XMLHttpRequest.prototype.send = function(data) {
        if (this._url && this._url.includes('admin-ajax')) {
            window.capturedRequests.push({
                type: 'XHR',
                method: this._method,
                url: this._url,
                data: data
            });
            console.log('XHR CAPTURED:', this._method, this._url, data);
        }
        return originalXHRSend.apply(this, arguments);
    };
    
    // Intercept Fetch
    const originalFetch = window.fetch;
    window.fetch = function(url, options) {
        if (url.includes('admin-ajax')) {
            window.capturedRequests.push({
                type: 'Fetch',
                method: (options && options.method) || 'GET',
                url: url,
                data: (options && options.body) || null
            });
            console.log('FETCH CAPTURED:', url, options);
        }
        return originalFetch.apply(this, arguments);
    };
    
    console.log('Capture script installed!');
""")

print("\nWaiting for form...")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'form'))
)
time.sleep(2)

print("\nClicking option...")
labels = driver.find_elements(By.TAG_NAME, 'label')
for label in labels:
    try:
        if 'ashutosh' in label.text.lower() and 'pratap' in label.text.lower():
            print(f"Found: {label.text}")
            label.click()
            break
    except:
        continue

time.sleep(1)

print("\nSubmitting form...")
submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
submit.click()

print("\nWaiting for AJAX request...")
time.sleep(5)

# Get captured requests
captured = driver.execute_script("return window.capturedRequests;")

print("\n" + "="*70)
print("CAPTURED REQUESTS:")
print("="*70)

if captured:
    for req in captured:
        print(f"\nType: {req['type']}")
        print(f"Method: {req['method']}")
        print(f"URL: {req['url']}")
        print(f"Data: {req['data']}")
        
        if req['data']:
            # Parse the data
            print("\n--- PARSED DATA ---")
            data_str = req['data']
            params = {}
            for pair in data_str.split('&'):
                if '=' in pair:
                    key, value = pair.split('=', 1)
                    params[key] = value
            print(json.dumps(params, indent=2))
else:
    print("\nNo AJAX requests captured!")
    print("Form might use standard POST instead of AJAX")

print("\n" + "="*70)

# Try to get the form action URL
form = driver.find_element(By.TAG_NAME, 'form')
print(f"\nForm action attribute: {form.get_attribute('action')}")
print(f"Form method: {form.get_attribute('method')}")

# Get current URL after submit
print(f"Current URL: {driver.current_url}")

# Check page source for any API endpoint
page_source = driver.page_source
if 'admin-ajax.php' in page_source:
    print("\n✓ Found admin-ajax.php in page source")
    print("This is a WordPress AJAX endpoint")

input("\nPress Enter to close...")
driver.quit()

print("\n\n" + "="*70)
print("SUMMARY")
print("="*70)
if captured:
    print("\n✓ We can make direct API calls!")
    print("We have the URL and data format.")
    print("Can create super-fast voter using requests library.")
else:
    print("\n✗ No AJAX captured")
    print("Form uses standard POST - harder to automate without browser")
