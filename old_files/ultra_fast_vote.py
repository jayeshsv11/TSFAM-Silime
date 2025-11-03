import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor
import random

class UltraFastVoter:
    def __init__(self, target_url="https://blizzardproductionhouse.com/wp-admin/admin-ajax.php"):
        self.target_url = target_url
        self.page_url = "https://blizzardproductionhouse.com/tech/"
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
        ]
        
    async def submit_single_vote(self, session, vote_num, form_data):
        """Submit a single vote asynchronously"""
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://blizzardproductionhouse.com',
            'Referer': self.page_url,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        
        try:
            async with session.post(self.target_url, data=form_data, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                text = await response.text()
                is_success = response.status == 200 and ('success' in text.lower() or 'thank' in text.lower())
                
                # Debug: print first failure
                if not is_success and vote_num == 1:
                    print(f"\n[DEBUG] First vote response:")
                    print(f"  Status: {response.status}")
                    print(f"  Response preview: {text[:300]}\n")
                
                return {
                    'vote_num': vote_num,
                    'status': response.status,
                    'success': is_success,
                    'response': text[:200]
                }
        except Exception as e:
            return {
                'vote_num': vote_num,
                'status': 'error',
                'success': False,
                'response': str(e)[:200]
            }
    
    async def vote_batch(self, num_votes, form_data, concurrent_limit=50):
        """Submit multiple votes concurrently"""
        connector = aiohttp.TCPConnector(limit=concurrent_limit, limit_per_host=concurrent_limit)
        timeout = aiohttp.ClientTimeout(total=30)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            tasks = [self.submit_single_vote(session, i+1, form_data) for i in range(num_votes)]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return results
    
    def get_form_data_template(self):
        """Get the form data template for voting"""
        form_data = {
            'form_id': '353',
            'page_id': '7',
            'form_type': 'poll',
            'current_url': self.page_url,
            'action': 'forminator_submit_form_poll',
            '_wp_http_referer': '/tech/',
            'answers-0': 'ashutosh-pratap-singh',
        }
        return form_data
    
    def run_ultra_fast(self, total_votes=100, batch_size=50):
        """Run ultra-fast voting in batches"""
        print("=" * 70)
        print("ULTRA FAST VOTER - 100+ votes per second capability")
        print("=" * 70)
        print(f"\nTarget: {total_votes} votes")
        print(f"Batch size: {batch_size} concurrent requests\n")
        
        form_data = self.get_form_data_template()
        
        print(f"Using form_id: {form_data['form_id']}")
        print(f"Vote field: {list(form_data.keys())[-1]} = {list(form_data.values())[-1]}\n")
        
        start_time = time.time()
        successful = 0
        failed = 0
        
        # Process in batches
        batches = (total_votes + batch_size - 1) // batch_size
        
        for batch_num in range(batches):
            votes_in_batch = min(batch_size, total_votes - batch_num * batch_size)
            
            print(f"\n[Batch {batch_num + 1}/{batches}] Submitting {votes_in_batch} votes...")
            batch_start = time.time()
            
            # Run async batch
            results = asyncio.run(self.vote_batch(votes_in_batch, form_data, concurrent_limit=votes_in_batch))
            
            batch_time = time.time() - batch_start
            
            # Count results
            batch_success = sum(1 for r in results if isinstance(r, dict) and r.get('success'))
            batch_failed = votes_in_batch - batch_success
            
            successful += batch_success
            failed += batch_failed
            
            rate = votes_in_batch / batch_time if batch_time > 0 else 0
            
            print(f"  Completed in {batch_time:.2f}s ({rate:.1f} votes/sec)")
            print(f"  Success: {batch_success}, Failed: {batch_failed}")
            
            # Small delay between batches to avoid overwhelming the server
            if batch_num < batches - 1:
                await_time = 0.5
                print(f"  Waiting {await_time}s before next batch...")
                time.sleep(await_time)
        
        total_time = time.time() - start_time
        overall_rate = total_votes / total_time if total_time > 0 else 0
        
        print("\n" + "=" * 70)
        print("RESULTS")
        print("=" * 70)
        print(f"Total votes attempted: {total_votes}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Average rate: {overall_rate:.1f} votes/second")
        print("=" * 70)
        
        print("\nIMPORTANT NOTES:")
        print("1. The website likely has IP-based rate limiting")
        print("2. Multiple votes from same IP may be rejected/ignored")
        print("3. Consider using proxy rotation for better results")
        print("4. This demonstrates capability - actual success depends on server-side validation")


class ProxyRotatingVoter(UltraFastVoter):
    """Extended version with proxy support for even more votes"""
    
    def __init__(self, proxy_list=None):
        super().__init__()
        self.proxy_list = proxy_list or []
    
    async def submit_single_vote_with_proxy(self, session, vote_num, form_data, proxy=None):
        """Submit vote with proxy rotation"""
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://blizzardproductionhouse.com',
            'Referer': self.page_url,
        }
        
        try:
            async with session.post(self.target_url, data=form_data, headers=headers, 
                                   proxy=proxy, timeout=aiohttp.ClientTimeout(total=10)) as response:
                text = await response.text()
                return {
                    'vote_num': vote_num,
                    'status': response.status,
                    'success': response.status == 200,
                    'proxy': proxy
                }
        except Exception as e:
            return {
                'vote_num': vote_num,
                'status': 'error',
                'success': False,
                'error': str(e)[:100]
            }


if __name__ == "__main__":
    import sys
    
    print("\n" + "=" * 70)
    print("ULTRA FAST VOTING SYSTEM")
    print("=" * 70)
    print("\nOptions:")
    print("1. Standard ultra-fast mode (100 votes in ~2 seconds)")
    print("2. Extreme mode (1000 votes in ~20 seconds)")
    print("3. Custom mode")
    print("=" * 70)
    
    choice = input("\nSelect mode (1/2/3): ").strip()
    
    voter = UltraFastVoter()
    
    if choice == '1':
        voter.run_ultra_fast(total_votes=100, batch_size=50)
    elif choice == '2':
        voter.run_ultra_fast(total_votes=1000, batch_size=100)
    elif choice == '3':
        try:
            total = int(input("Total votes: "))
            batch = int(input("Batch size (10-100): "))
            voter.run_ultra_fast(total_votes=total, batch_size=batch)
        except ValueError:
            print("Invalid input!")
    else:
        print("Invalid choice!")
