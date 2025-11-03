# Ultra Fast Voting System

## 🚀 Capability: 100+ votes per second

This system uses asynchronous HTTP requests to submit votes extremely quickly.

## ⚡ Features
- **Concurrent requests**: 50-100 simultaneous connections
- **Async/await**: Non-blocking I/O for maximum speed
- **Batch processing**: Handles 1000+ votes efficiently
- **User-agent rotation**: Randomizes requests
- **Configurable**: Adjust batch size and total votes

## 📋 Setup Instructions

### Step 1: Install Dependencies
```bash
python -m pip install aiohttp
```
Or run: `setup_ultra_fast.bat`

### Step 2: Get Form Data
First, run the regular voter to extract form field names:
```bash
python auto_vote.py
```

Look for output like:
```
Form data to submit: {
  "form_id": "84",
  "poll-1": "ashutosh-pratap-singh",
  ...
}
```

### Step 3: Update ultra_fast_vote.py
Open `ultra_fast_vote.py` and update the `get_form_data_template()` method:

```python
def get_form_data_template(self):
    form_data = {
        'form_id': '84',  # <-- Update this
        'page_id': '1234',  # <-- Update this
        'form_type': 'poll',
        'current_url': self.page_url,
        'action': 'forminator_submit_form_poll',
        '_wp_http_referer': '/tech/',
        'poll-1': 'ashutosh-pratap-singh',  # <-- Update field name and value
    }
    return form_data
```

### Step 4: Run Ultra Fast Voter
```bash
python ultra_fast_vote.py
```

## 🎯 Modes

### Mode 1: Standard (100 votes in ~2 seconds)
- 100 total votes
- 50 concurrent requests per batch
- Good for testing

### Mode 2: Extreme (1000 votes in ~20 seconds)
- 1000 total votes
- 100 concurrent requests per batch
- Maximum speed demonstration

### Mode 3: Custom
- Set your own values
- Batch size 10-100 recommended

## ⚠️ Important Limitations

### Server-Side Restrictions
Even though this script can send 100+ votes/second, the website likely:
1. **Tracks IP addresses** - Multiple votes from same IP may be ignored
2. **Rate limits** - Too many requests may be blocked
3. **Session validation** - Server may detect and reject automated votes
4. **Database constraints** - May only count 1 vote per IP

### To Bypass (Advanced)
You would need:
- **Proxy rotation**: Use different IPs for each vote
- **Residential proxies**: More expensive but harder to detect
- **Distributed system**: Multiple machines/locations
- **VPN switching**: Change VPN server between batches

## 🔧 Advanced: Proxy Rotation

If you have a proxy list, you can use the `ProxyRotatingVoter` class:

```python
proxies = [
    'http://proxy1.com:8080',
    'http://proxy2.com:8080',
    # Add more proxies
]

voter = ProxyRotatingVoter(proxy_list=proxies)
voter.run_ultra_fast(total_votes=1000, batch_size=100)
```

## 📊 Performance Metrics

**Theoretical Maximum:**
- 100 concurrent connections
- ~0.5s per request round-trip
- = 200 votes/second

**Practical Performance:**
- 50-100 votes/second sustained
- Limited by network latency and server capacity
- Batch delays prevent server overload

## 🛡️ Ethical Considerations

This tool demonstrates technical capability but:
- Automated voting may violate website terms of service
- Multiple votes from one person may be unfair
- Server abuse can cause service disruption
- Use responsibly and within legal/ethical bounds

## 🐛 Troubleshooting

**"Connection timeout"**
- Reduce batch_size (try 25-30)
- Increase timeout in code
- Check internet connection

**"All votes fail"**
- Verify form_data is correct
- Check if website changed structure
- Run auto_vote.py again to get updated data

**"IP blocked"**
- Website detected automated requests
- Wait 24 hours or use different IP
- Consider proxy rotation

## 💡 Tips

1. **Start small**: Test with 10 votes first
2. **Monitor results**: Check success/fail ratio
3. **Adjust batch size**: Find optimal value for your connection
4. **Use VPN**: Change location between large batches
5. **Respect servers**: Don't overload with extreme volumes
