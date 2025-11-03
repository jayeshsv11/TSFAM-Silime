import requests
from bs4 import BeautifulSoup
import re
import json

print("="*70)
print("DEEP DIAGNOSTIC - Testing actual vote submission")
print("="*70)

url = 'https://blizzardproductionhouse.com/tech/'
ajax_url = "https://blizzardproductionhouse.com/wp-admin/admin-ajax.php"

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# Step 1: Get the page
print("\n[1] Fetching page to get form details...")
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Find the form
poll_form = soup.find('form', {'class': re.compile(r'forminator')})

if not poll_form:
    print("❌ No form found!")
    exit()

form_id_full = poll_form.get('id', '')
form_id = form_id_full.replace('forminator-module-', '')
print(f"✓ Form found: {form_id_full} (ID: {form_id})")

# Step 3: Look for all form fields
print("\n[2] Analyzing form structure...")
all_inputs = poll_form.find_all('input')
print(f"Total input fields: {len(all_inputs)}")

for inp in all_inputs:
    inp_type = inp.get('type', '')
    inp_name = inp.get('name', '')
    inp_value = inp.get('value', '')
    if inp_name:
        print(f"  - {inp_type}: {inp_name} = {inp_value}")

# Step 4: Check page source for JavaScript data
print("\n[3] Checking for JavaScript poll data...")
if 'forminator' in response.text:
    # Look for poll options in JSON format
    json_match = re.search(r'var forminator.*?=\s*({.*?});', response.text, re.DOTALL)
    if json_match:
        print("✓ Found forminator JavaScript data")
    
    # Look for poll answers
    if 'answers' in response.text.lower():
        answers_matches = re.findall(r'"answer[^"]*":\s*"([^"]+)"', response.text)
        if answers_matches:
            print(f"✓ Found {len(answers_matches)} answer options in source:")
            for ans in answers_matches[:5]:
                print(f"    - {ans}")

# Step 5: Try to submit a test vote
print("\n[4] Attempting test vote submission...")

# Try multiple field name variations
test_payloads = [
    {
        'form_id': form_id,
        'page_id': '7',
        'form_type': 'poll',
        'current_url': url,
        'action': 'forminator_submit_form_poll',
        '_wp_http_referer': '/tech/',
        'answers-0': 'ashutosh-pratap-singh',
    },
    {
        'form_id': form_id,
        'answers[0]': 'ashutosh-pratap-singh',
        'action': 'forminator_submit_form_poll',
        '_wp_http_referer': '/tech/',
    },
    {
        'form_id': form_id,
        f'poll-{form_id}': 'ashutosh-pratap-singh',
        'action': 'forminator_submit_form_poll',
    },
]

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://blizzardproductionhouse.com',
    'Referer': url,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

for idx, payload in enumerate(test_payloads):
    print(f"\n--- Test {idx+1} ---")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    response = session.post(ajax_url, data=payload, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}")
    
    if response.status_code == 200:
        try:
            resp_json = response.json()
            print(f"\nJSON Response: {json.dumps(resp_json, indent=2)}")
        except:
            pass
    
    if 'success' in response.text.lower():
        print("\n✓✓✓ THIS PAYLOAD WORKS! ✓✓✓")
        break
    elif 'error' in response.text.lower() or 'invalid' in response.text.lower():
        print("❌ Error in response")
    
    print()

print("\n" + "="*70)
print("DIAGNOSTIC COMPLETE")
print("="*70)
