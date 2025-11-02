import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://blizzardproductionhouse.com/tech/'
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

print('='*70)
print('FORM DATA EXTRACTOR - Getting real form values')
print('='*70)
print('\nFetching page...')
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

poll_form = soup.find('form', {'class': re.compile(r'forminator')})

if poll_form:
    form_id_full = poll_form.get('id', '')
    form_id_num = form_id_full.replace('forminator-module-', '') if 'forminator-module-' in form_id_full else form_id_full
    
    print(f'\n✓ Found form: {form_id_full}')
    print(f'  Form ID number: {form_id_num}')
    
    # Get all form elements
    all_inputs = poll_form.find_all('input')
    all_labels = poll_form.find_all('label')
    
    print(f'\n  Total inputs: {len(all_inputs)}')
    print(f'  Total labels: {len(all_labels)}')
    
    # Try to find the poll answer field name
    print('\nSearching for poll field name...')
    answer_field = None
    for inp in all_inputs:
        name = inp.get('name', '')
        if 'answer' in name or 'poll' in name or 'radio' in name:
            answer_field = name
            print(f'  Found field: {name}')
    
    if not answer_field:
        # Look in page source for answer field pattern
        if 'answers-' in response.text:
            match = re.search(r'name=["\']([^"\']*answers[^"\']*)["\']', response.text)
            if match:
                answer_field = match.group(1)
                print(f'  Found in source: {answer_field}')
    
    # Try to find page_id
    page_id = None
    for inp in all_inputs:
        if inp.get('name') == 'page_id':
            page_id = inp.get('value')
            break
    
    if not page_id:
        # Try to extract from URL or meta
        import urllib.parse
        if '?p=' in url or '?page_id=' in url:
            parsed = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            page_id = parsed.get('p', [None])[0] or parsed.get('page_id', [None])[0]
    
    print(f'\nPage ID: {page_id if page_id else "Not found - will try dynamic"}')
    
    # Generate the form_data template
    print('\n' + '='*70)
    print('UPDATE ultra_fast_vote.py WITH THIS DATA:')
    print('='*70)
    print('\nReplace get_form_data_template() with:\n')
    print('def get_form_data_template(self):')
    print('    form_data = {')
    print(f'        \'form_id\': \'{form_id_num}\',')
    print(f'        \'page_id\': \'{page_id if page_id else "7"}\',  # May need manual update')
    print('        \'form_type\': \'poll\',')
    print('        \'current_url\': self.page_url,')
    print('        \'action\': \'forminator_submit_form_poll\',')
    print('        \'_wp_http_referer\': \'/tech/\',')
    if answer_field:
        print(f'        \'{answer_field}\': \'ashutosh-pratap-singh\',  # Update value if needed')
    else:
        print('        \'answers-0\': \'ashutosh-pratap-singh\',  # UPDATE THIS FIELD NAME!')
    print('    }')
    print('    return form_data')
    print('\n' + '='*70)
    
else:
    print('\n✗ Form not found!')
    print('The page may use JavaScript to load the form dynamically.')
    print('Try using Selenium-based script instead.')
