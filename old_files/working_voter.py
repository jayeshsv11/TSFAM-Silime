import requests
from bs4 import BeautifulSoup
import re
import json

class WorkingVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.ajax_url = "https://blizzardproductionhouse.com/wp-admin/admin-ajax.php"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
    
    def get_nonce_and_form_data(self):
        """Fetch page and extract nonce + form data"""
        print("Fetching page to get nonce...")
        response = self.session.get(self.url)
        
        # Look for nonce in page source
        # Common patterns: forminator_nonce, _wpnonce, etc.
        nonce = None
        
        # Pattern 1: Look for nonce in script/JSON data
        nonce_match = re.search(r'"nonce"\s*:\s*"([^"]+)"', response.text)
        if nonce_match:
            nonce = nonce_match.group(1)
            print(f"✓ Found nonce in JSON: {nonce}")
        
        # Pattern 2: Look in form input
        if not nonce:
            soup = BeautifulSoup(response.text, 'html.parser')
            nonce_input = soup.find('input', {'name': re.compile(r'nonce|_wpnonce', re.I)})
            if nonce_input:
                nonce = nonce_input.get('value')
                print(f"✓ Found nonce in input: {nonce}")
        
        # Pattern 3: Look for forminator specific nonce
        if not nonce:
            nonce_match = re.search(r'forminator.*nonce.*?["\']([a-f0-9]{10,})["\']', response.text, re.I)
            if nonce_match:
                nonce = nonce_match.group(1)
                print(f"✓ Found forminator nonce: {nonce}")
        
        # Pattern 4: Any nonce-like pattern in the HTML
        if not nonce:
            soup = BeautifulSoup(response.text, 'html.parser')
            poll_form = soup.find('form', {'class': re.compile(r'forminator')})
            if poll_form:
                # Get all input values that look like nonces (long alphanumeric)
                all_inputs = poll_form.find_all('input')
                for inp in all_inputs:
                    val = inp.get('value', '')
                    if len(val) > 10 and re.match(r'^[a-f0-9]+$', val):
                        nonce = val
                        print(f"✓ Found potential nonce: {nonce}")
                        break
        
        return nonce
    
    def submit_vote(self, nonce=None):
        """Submit vote with nonce"""
        form_data = {
            'form_id': '353',
            'page_id': '7',
            'form_type': 'poll',
            'current_url': self.url,
            'action': 'forminator_submit_form_poll',
            '_wp_http_referer': '/tech/',
            'answers-0': 'ashutosh-pratap-singh',
        }
        
        if nonce:
            form_data['_wpnonce'] = nonce
            form_data['forminator_nonce'] = nonce
        
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://blizzardproductionhouse.com',
            'Referer': self.url,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        
        print(f"\nSubmitting vote...")
        print(f"Form data: {json.dumps(form_data, indent=2)}")
        
        response = self.session.post(self.ajax_url, data=form_data, headers=headers)
        
        print(f"\nStatus: {response.status_code}")
        print(f"Response: {response.text}")
        
        try:
            resp_json = response.json()
            if resp_json.get('success'):
                print("\n✓✓✓ VOTE SUCCESSFUL! ✓✓✓")
                return True
            else:
                print(f"\n❌ Vote failed: {resp_json.get('data', 'Unknown error')}")
                return False
        except:
            print(f"\n? Response not JSON")
            return False
    
    def vote(self):
        """Main voting function"""
        # Clear cookies to simulate new visitor
        self.session.cookies.clear()
        
        # Get nonce
        nonce = self.get_nonce_and_form_data()
        
        if not nonce:
            print("\n⚠ Warning: No nonce found, trying without it...")
        
        # Submit vote
        return self.submit_vote(nonce)


if __name__ == "__main__":
    print("="*70)
    print("FIXED VOTER - With Nonce Support")
    print("Voting for: Ashutosh Pratap Singh")
    print("="*70)
    print()
    
    voter = WorkingVoter()
    
    # Try voting
    success = voter.vote()
    
    if success:
        print("\n" + "="*70)
        print("SUCCESS! Vote was counted.")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("FAILED - Need to investigate further")
        print("="*70)
