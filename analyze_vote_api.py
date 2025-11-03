"""
Analyze what happens when vote button is clicked
Check if we can bypass browser and just call API directly
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

# Enable browser logging
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

driver = webdriver.Chrome(options=options)

print("="*70)
print("ANALYZING VOTE SUBMISSION")
print("="*70)
print("\nOpening voting page...")

driver.get("https://blizzardproductionhouse.com/tech/")
time.sleep(3)

print("\nWaiting for form...")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'form'))
)
time.sleep(2)

# Get form details
forms = driver.find_elements(By.TAG_NAME, 'form')
if forms:
    form = forms[0]
    print(f"\nForm found!")
    print(f"Action: {form.get_attribute('action')}")
    print(f"Method: {form.get_attribute('method')}")
    print(f"Class: {form.get_attribute('class')}")
    print(f"ID: {form.get_attribute('id')}")

# Get all inputs
inputs = driver.find_elements(By.TAG_NAME, 'input')
print(f"\n{len(inputs)} input fields found:")
for i, inp in enumerate(inputs):
    print(f"  [{i}] Type: {inp.get_attribute('type')}, Name: {inp.get_attribute('name')}, Value: {inp.get_attribute('value')}")

# Click option
print("\nClicking Ashutosh Pratap Singh...")
labels = driver.find_elements(By.TAG_NAME, 'label')
for label in labels:
    try:
        text = label.text.lower()
        if 'ashutosh' in text and 'pratap' in text:
            print(f"Found: {label.text}")
            label.click()
            break
    except:
        continue

time.sleep(1)

# Get form data before submit
print("\nForm data before submit:")
inputs = driver.find_elements(By.TAG_NAME, 'input')
form_data = {}
for inp in inputs:
    name = inp.get_attribute('name')
    value = inp.get_attribute('value')
    inp_type = inp.get_attribute('type')
    if name:
        if inp_type == 'radio':
            if inp.is_selected():
                form_data[name] = value
        else:
            form_data[name] = value

print(json.dumps(form_data, indent=2))

# Inject JavaScript to capture form submission
print("\nInjecting capture script...")
driver.execute_script("""
    window.capturedData = null;
    window.capturedUrl = null;
    
    // Capture form submit
    document.querySelector('form').addEventListener('submit', function(e) {
        window.capturedUrl = this.action;
        let formData = new FormData(this);
        let data = {};
        for (let [key, value] of formData.entries()) {
            data[key] = value;
        }
        window.capturedData = data;
        console.log('FORM SUBMIT:', data);
    });
    
    // Capture AJAX requests
    const originalFetch = window.fetch;
    window.fetch = function() {
        console.log('FETCH:', arguments[0]);
        return originalFetch.apply(this, arguments);
    };
    
    const originalXHR = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function() {
        console.log('XHR:', arguments[1]);
        return originalXHR.apply(this, arguments);
    };
""")

# Submit
print("\nSubmitting form...")
submit = driver.find_element(By.CLASS_NAME, 'forminator-button-submit')
submit.click()

time.sleep(4)

# Get captured data
captured_url = driver.execute_script("return window.capturedUrl;")
captured_data = driver.execute_script("return window.capturedData;")

print("\n" + "="*70)
print("CAPTURED SUBMISSION DATA:")
print("="*70)
print(f"\nURL: {captured_url}")
print(f"\nData:")
print(json.dumps(captured_data, indent=2))

# Get network logs
print("\n" + "="*70)
print("NETWORK REQUESTS:")
print("="*70)
logs = driver.get_log('performance')
for log in logs:
    message = json.loads(log['message'])
    method = message.get('message', {}).get('method', '')
    
    if 'Network.request' in method or 'Network.response' in method:
        params = message.get('message', {}).get('params', {})
        request = params.get('request', {})
        response = params.get('response', {})
        
        if request:
            url = request.get('url', '')
            if 'blizzard' in url or 'forminator' in url or 'tech' in url:
                print(f"\nRequest: {request.get('method', '')} {url}")
                if request.get('postData'):
                    print(f"POST Data: {request.get('postData')}")
                if request.get('headers'):
                    print(f"Headers: {json.dumps(request.get('headers'), indent=2)}")

print("\n" + "="*70)
print("ANALYSIS COMPLETE")
print("="*70)

input("\nPress Enter to close browser...")
driver.quit()

print("\n\nConclusion:")
print("If captured URL and data are shown above,")
print("we can try making direct HTTP POST requests!")
