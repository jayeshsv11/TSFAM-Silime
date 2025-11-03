"""
MOBILE HOTSPOT AUTO-VOTER
Optimized for mobile hotspot IP rotation via airplane mode toggle
"""
import time
import os
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import threading

class MobileHotspotVoter:
    def __init__(self):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.lock = threading.Lock()
        self.total_votes = 0
        self.total_successful = 0
        self.total_failed = 0
        self.current_ip = "Unknown"
        
    def beep(self):
        """Make a beep sound"""
        try:
            # Windows beep
            import winsound
            winsound.Beep(1000, 500)  # 1000 Hz for 500ms
        except:
            # Fallback: print bell character
            print('\a')
    
    def get_current_ip(self):
        """Get current IP address"""
        try:
            import requests
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            return response.json().get('ip', 'Unknown')
        except:
            return "Unknown"
    
    def vote_once_fast(self, vote_num):
        """Optimized single vote for mobile connection"""
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        options.page_load_strategy = 'eager'  # Faster loading
        
        driver = webdriver.Chrome(options=options)
        
        try:
            driver.set_page_load_timeout(15)
            driver.get(self.url)
            
            # Quick wait for form
            time.sleep(1.5)
            
            # Find and click option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            for label in labels:
                try:
                    if 'ashutosh' in label.text.lower() and 'pratap' in label.text.lower():
                        driver.execute_script("arguments[0].click();", label)
                        break
                except:
                    continue
            
            time.sleep(0.3)
            
            # Submit
            submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            driver.execute_script("arguments[0].click();", submit)
            
            time.sleep(2)
            
            success = 'thank' in driver.page_source.lower() or 'success' in driver.page_source.lower()
            
            with self.lock:
                if success:
                    self.total_successful += 1
                    print(f"  [{vote_num}] ✓")
                else:
                    self.total_failed += 1
                    print(f"  [{vote_num}] ✗")
            
            return success
                 
        except Exception as e:
            with self.lock:
                self.total_failed += 1
            print(f"  [{vote_num}] ✗ {str(e)[:30]}")
            return False
        finally:
            driver.quit()
    
    def vote_batch_parallel(self, num_votes, workers=3):
        """Vote with parallel workers (optimized for mobile)"""
        print(f"\n🔄 Voting {num_votes} times with {workers} parallel browsers...")
        print(f"⏱  Started at: {datetime.now().strftime('%H:%M:%S')}")
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=workers) as executor:
            list(executor.map(self.vote_once_fast, range(1, num_votes + 1)))
        
        elapsed = time.time() - start_time
        
        print(f"\n✅ Batch complete in {elapsed:.1f}s")
        print(f"   Successful: {self.total_successful}")
        print(f"   Failed: {self.total_failed}")
        
        return self.total_successful, self.total_failed
    
    def run_with_ip_rotation(self, votes_per_ip=5, total_ips=20, workers=3):
        """Main voting loop with IP rotation prompts"""
        
        print("="*70)
        print("🔥 MOBILE HOTSPOT AUTO-VOTER")
        print("="*70)
        print()
        print(f"Configuration:")
        print(f"  - Votes per IP: {votes_per_ip}")
        print(f"  - Target IPs: {total_ips}")
        print(f"  - Total votes: {votes_per_ip * total_ips}")
        print(f"  - Parallel workers: {workers}")
        print()
        print("="*70)
        print("📱 MOBILE HOTSPOT INSTRUCTIONS:")
        print("="*70)
        print()
        print("When prompted:")
        print("  1. Toggle AIRPLANE MODE on your phone")
        print("     - Turn ON → wait 3 seconds → Turn OFF")
        print("  2. Wait for laptop to reconnect (~10 seconds)")
        print("  3. Press Enter to continue voting")
        print()
        print("="*70)
        input("\nPress Enter when ready to start...")
        
        overall_start = time.time()
        
        for ip_num in range(1, total_ips + 1):
            print()
            print("="*70)
            print(f"📍 IP #{ip_num}/{total_ips}")
            print("="*70)
            
            # Get and display current IP
            self.current_ip = self.get_current_ip()
            print(f"Current IP: {self.current_ip}")
            
            # Vote batch
            success, failed = self.vote_batch_parallel(votes_per_ip, workers)
            
            self.total_votes += votes_per_ip
            
            # Show progress
            print()
            print(f"📊 Overall Progress:")
            print(f"   Total votes submitted: {self.total_votes}")
            print(f"   Total successful: {self.total_successful}")
            print(f"   Total IPs used: {ip_num}")
            print(f"   Elapsed time: {(time.time() - overall_start)/60:.1f} minutes")
            
            # Prompt for IP change (except on last iteration)
            if ip_num < total_ips:
                print()
                print("="*70)
                print("🔄 TIME TO CHANGE IP!")
                print("="*70)
                print()
                print("📱 On your phone:")
                print("   1. Toggle AIRPLANE MODE ON")
                print("   2. Wait 3 seconds")
                print("   3. Toggle AIRPLANE MODE OFF")
                print("   4. Wait for connection (~10 seconds)")
                print()
                
                # Make beeping sound to alert user
                self.beep()
                
                next_ip = input("\n✋ Press Enter when reconnected to continue... ")
                
                # Verify IP changed
                new_ip = self.get_current_ip()
                if new_ip == self.current_ip:
                    print()
                    print("⚠️  WARNING: IP appears unchanged!")
                    print(f"   Previous: {self.current_ip}")
                    print(f"   Current:  {new_ip}")
                    print()
                    retry = input("   Toggle airplane mode again? (y/n): ")
                    if retry.lower() == 'y':
                        input("   Press Enter when reconnected... ")
                else:
                    print(f"✅ IP changed! {self.current_ip} → {new_ip}")
        
        # Final summary
        total_time = time.time() - overall_start
        
        print()
        print("="*70)
        print("🎉 VOTING COMPLETE!")
        print("="*70)
        print()
        print(f"📊 Final Statistics:")
        print(f"   Total votes submitted: {self.total_votes}")
        print(f"   Successful votes: {self.total_successful}")
        print(f"   Failed votes: {self.total_failed}")
        print(f"   IPs used: {total_ips}")
        print(f"   Total time: {total_time/60:.1f} minutes")
        print(f"   Average: {self.total_successful/(total_time/60):.1f} real votes/minute")
        print()
        print("="*70)


if __name__ == "__main__":
    print()
    print("="*70)
    print("MOBILE HOTSPOT VOTER - SETUP")
    print("="*70)
    print()
    print("This script is optimized for mobile hotspot connections.")
    print("It will prompt you to change IP between batches.")
    print()
    print("Recommended settings:")
    print("  - Small batches (3-5 votes)")
    print("  - Few workers (2-3)")
    print("  - Many IP rotations (20+)")
    print()
    print("="*70)
    print()
    
    try:
        # Get user preferences
        votes_per_ip = int(input("Votes per IP (3-10, default 5): ") or "5")
        total_ips = int(input("How many IPs to use (10-50, default 20): ") or "20")
        workers = int(input("Parallel workers (2-5, default 3): ") or "3")
        
        voter = MobileHotspotVoter()
        voter.run_with_ip_rotation(votes_per_ip, total_ips, workers)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Stopped by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
