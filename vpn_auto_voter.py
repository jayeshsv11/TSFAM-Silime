"""
VPN AUTO-SWITCHER + CONTINUOUS VOTER
Switches VPN servers automatically between votes
Supports popular VPN providers
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import subprocess
import time
import os
from datetime import datetime

class VPNAutoSwitcher:
    """
    Auto-switch VPN for different IP addresses
    
    SETUP REQUIRED:
    1. Install VPN client (NordVPN, ExpressVPN, ProtonVPN, etc.)
    2. Make sure VPN command-line tools are installed
    """
    
    def __init__(self, vpn_type="nordvpn"):
        self.vpn_type = vpn_type.lower()
        
    def switch_server(self):
        """Switch to a random VPN server"""
        try:
            if self.vpn_type == "nordvpn":
                # NordVPN CLI commands
                subprocess.run(["nordvpn", "disconnect"], capture_output=True, timeout=10)
                time.sleep(2)
                subprocess.run(["nordvpn", "connect"], capture_output=True, timeout=30)
                time.sleep(5)
                return True
                
            elif self.vpn_type == "expressvpn":
                # ExpressVPN CLI
                subprocess.run(["expressvpn", "disconnect"], capture_output=True, timeout=10)
                time.sleep(2)
                subprocess.run(["expressvpn", "connect", "smart"], capture_output=True, timeout=30)
                time.sleep(5)
                return True
                
            elif self.vpn_type == "protonvpn":
                # ProtonVPN CLI
                subprocess.run(["protonvpn", "disconnect"], capture_output=True, timeout=10)
                time.sleep(2)
                subprocess.run(["protonvpn", "connect", "-f"], capture_output=True, timeout=30)
                time.sleep(5)
                return True
                
            elif self.vpn_type == "manual":
                # Manual VPN switching - user does it
                print("\n" + "="*70)
                print("⚠ MANUAL VPN SWITCH REQUIRED")
                print("="*70)
                print("Please switch your VPN server now:")
                print("1. Open your VPN app")
                print("2. Disconnect from current server")
                print("3. Connect to a DIFFERENT server/country")
                print("4. Wait for connection to establish")
                input("\nPress Enter when VPN is connected to new server...")
                return True
            else:
                print(f"Unknown VPN type: {self.vpn_type}")
                return False
                
        except Exception as e:
            print(f"VPN switch failed: {str(e)}")
            return False
    
    def get_current_ip(self):
        """Get current IP address"""
        try:
            import requests
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            return response.json().get('ip', 'Unknown')
        except:
            return "Unknown"


class VPNAutoVoter:
    def __init__(self, vpn_switcher):
        self.url = "https://blizzardproductionhouse.com/tech/"
        self.vpn = vpn_switcher
        self.total_successful = 0
        self.total_failed = 0
        self.total_attempts = 0
        
    def vote_once(self):
        """Single vote attempt"""
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        
        driver = webdriver.Chrome(options=options)
        
        try:
            driver.set_page_load_timeout(10)
            driver.get(self.url)
            time.sleep(1.5)
            
            # Click Ashutosh option
            labels = driver.find_elements(By.TAG_NAME, 'label')
            for label in labels:
                if 'ashutosh' in label.text.lower() and 'pratap' in label.text.lower():
                    driver.execute_script("arguments[0].click();", label)
                    break
            
            time.sleep(0.3)
            
            # Submit
            submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            driver.execute_script("arguments[0].click();", submit)
            time.sleep(2)
            
            return 'thank' in driver.page_source.lower() or 'success' in driver.page_source.lower()
                
        except Exception as e:
            return False
        finally:
            driver.quit()
    
    def run_with_vpn_switching(self, votes_per_switch=5, total_votes=None):
        """Vote with automatic VPN switching"""
        print("="*70)
        print("VPN AUTO-SWITCHING VOTER")
        print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
        print(f"Votes per VPN switch: {votes_per_switch}")
        print("="*70)
        
        current_ip = self.vpn.get_current_ip()
        print(f"\nCurrent IP: {current_ip}\n")
        
        vote_count_on_current_ip = 0
        
        try:
            while True:
                # Switch VPN if needed
                if vote_count_on_current_ip >= votes_per_switch:
                    print("\n" + "="*70)
                    print(f"Reached {votes_per_switch} votes, switching VPN...")
                    print("="*70)
                    
                    if self.vpn.switch_server():
                        new_ip = self.vpn.get_current_ip()
                        print(f"✓ VPN switched | New IP: {new_ip}")
                        vote_count_on_current_ip = 0
                    else:
                        print("✗ VPN switch failed, continuing anyway...")
                    
                    print()
                
                # Vote
                self.total_attempts += 1
                vote_count_on_current_ip += 1
                
                start = time.time()
                success = self.vote_once()
                elapsed = time.time() - start
                
                if success:
                    self.total_successful += 1
                    print(f"[{self.total_attempts}] ✓ SUCCESS | Time: {elapsed:.1f}s | Total: {self.total_successful}")
                else:
                    self.total_failed += 1
                    print(f"[{self.total_attempts}] ✗ FAILED | Time: {elapsed:.1f}s | Failed: {self.total_failed}")
                
                # Check if we've reached total
                if total_votes and self.total_attempts >= total_votes:
                    break
                    
        except KeyboardInterrupt:
            print("\n\nStopped by user")
        
        print("\n" + "="*70)
        print("FINAL RESULTS")
        print("="*70)
        print(f"Total attempts: {self.total_attempts}")
        print(f"Successful: {self.total_successful}")
        print(f"Failed: {self.total_failed}")
        if self.total_attempts > 0:
            print(f"Success rate: {(self.total_successful/self.total_attempts*100):.1f}%")
        print("="*70)


if __name__ == "__main__":
    print("="*70)
    print("VPN AUTO-SWITCHING CONTINUOUS VOTER")
    print("="*70)
    print("\nSelect VPN type:")
    print("1. NordVPN (CLI required)")
    print("2. ExpressVPN (CLI required)")
    print("3. ProtonVPN (CLI required)")
    print("4. Manual (You switch VPN manually)")
    print("="*70)
    
    choice = input("\nSelect (1-4): ").strip()
    
    vpn_map = {
        '1': 'nordvpn',
        '2': 'expressvpn',
        '3': 'protonvpn',
        '4': 'manual'
    }
    
    vpn_type = vpn_map.get(choice, 'manual')
    
    print(f"\nUsing: {vpn_type}")
    
    votes_per_switch = int(input("Votes per VPN switch (recommended: 3-5): ") or "5")
    
    total = input("Total votes (leave empty for continuous): ").strip()
    total_votes = int(total) if total else None
    
    print("\nStarting VPN auto-switching voter...")
    print("Press Ctrl+C to stop\n")
    
    vpn_switcher = VPNAutoSwitcher(vpn_type)
    voter = VPNAutoVoter(vpn_switcher)
    
    voter.run_with_vpn_switching(votes_per_switch=votes_per_switch, total_votes=total_votes)
