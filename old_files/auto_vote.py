import requests
from bs4 import BeautifulSoup
import re
import time
import json

class BlizzardAutoVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
    def get_form_data(self):
        """Fetch the page and extract form data"""
        print("Fetching page...")
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the poll form
        poll_form = soup.find('form', {'class': re.compile(r'forminator-poll')})
        
        if not poll_form:
            print("Could not find poll form")
            return None
            
        # Extract form ID
        form_id = poll_form.get('id', '')
        print(f"Found form: {form_id}")
        
        # Find all radio buttons/options
        options = poll_form.find_all('input', {'type': 'radio'})
        
        print("\nAvailable candidates:")
        for idx, option in enumerate(options):
            label = poll_form.find('label', {'for': option.get('id', '')})
            label_text = label.get_text(strip=True) if label else 'Unknown'
            print(f"{idx + 1}. {label_text} (value: {option.get('value', '')})")
        
        # Find Ashutosh Pratap Singh option
        ashutosh_option = None
        for option in options:
            option_value = option.get('value', '')
            label = poll_form.find('label', {'for': option.get('id', '')})
            label_text = label.get_text(strip=True) if label else ''
            
            # Check both label text and value
            if ('Ashutosh Pratap Singh' in label_text or 
                'Ashutosh Pratap Singh' in option_value or
                'ashutosh' in label_text.lower()):
                ashutosh_option = option
                break
        
        if not ashutosh_option:
            print("\nCould not find Ashutosh Pratap Singh option")
            return None
            
        print(f"\nFound Ashutosh Pratap Singh option!")
        
        # Extract form data
        form_data = {
            'form_id': form_id.replace('forminator-module-', ''),
            'page_id': soup.find('input', {'name': 'page_id'}).get('value') if soup.find('input', {'name': 'page_id'}) else '',
            'form_type': 'poll',
            'current_url': self.url,
            'action': 'forminator_submit_form_poll',
            '_wp_http_referer': '/tech/',
        }
        
        # Add the vote value
        answer_field = ashutosh_option.get('name', '')
        form_data[answer_field] = ashutosh_option.get('value', '')
        
        # Look for nonce
        nonce_input = poll_form.find('input', {'name': re.compile(r'nonce|_wpnonce|forminator_nonce')})
        if nonce_input:
            form_data[nonce_input.get('name')] = nonce_input.get('value')
        
        return form_data
    
    def submit_vote(self, form_data):
        """Submit the vote"""
        print("\nSubmitting vote...")
        
        ajax_url = "https://blizzardproductionhouse.com/wp-admin/admin-ajax.php"
        
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://blizzardproductionhouse.com',
            'Referer': self.url,
        }
        
        response = self.session.post(ajax_url, data=form_data, headers=headers)
        
        print(f"Response status: {response.status_code}")
        print(f"Response: {response.text[:500]}")
        
        return response
    
    def clear_cookies(self):
        """Clear cookies to vote again"""
        print("\nClearing cookies...")
        self.session.cookies.clear()
        
    def vote_for_ashutosh(self, clear_data=True):
        """Main function to vote for Ashutosh Pratap Singh"""
        if clear_data:
            self.clear_cookies()
        
        form_data = self.get_form_data()
        
        if form_data:
            print(f"\nForm data to submit: {json.dumps(form_data, indent=2)}")
            response = self.submit_vote(form_data)
            
            if response.status_code == 200:
                if 'success' in response.text.lower():
                    print("\n✓ Vote submitted successfully!")
                    return True
                elif 'already' in response.text.lower() and 'voted' in response.text.lower():
                    print("\n⚠ Already voted (tracked by IP or cookies)")
                    return False
                else:
                    print(f"\n✗ Unexpected response")
                    return False
            else:
                print(f"\n✗ Failed with status code {response.status_code}")
                return False
        else:
            print("\n✗ Could not extract form data")
            return False


if __name__ == "__main__":
    print("=" * 60)
    print("Blizzard Production House - Auto Voter")
    print("Voting for: Ashutosh Pratap Singh")
    print("=" * 60)
    
    voter = BlizzardAutoVoter()
    
    # Try voting with clearing cookies
    voter.vote_for_ashutosh(clear_data=True)
    
    print("\n" + "=" * 60)
    print("Note: The website likely tracks votes by:")
    print("1. Cookies (cleared by this script)")
    print("2. IP Address (requires VPN/proxy to bypass)")
    print("3. Browser fingerprint (requires different browsers)")
    print("=" * 60)
