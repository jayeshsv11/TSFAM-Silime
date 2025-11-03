"""
VOTE WITH 20 BROWSERS - Fast voting
"""
from simple_parallel_test import SimpleParallelVoter

if __name__ == "__main__":
    print("\n" + "="*70)
    print("VOTING WITH 20 PARALLEL BROWSERS")
    print("="*70)
    print("\nThis will open 20 Chrome browsers and vote!")
    print("Expected time: 60-90 seconds")
    print("\n" + "="*70)
    
    input("\nPress Enter to start...")
    
    voter = SimpleParallelVoter()
    voter.vote_parallel(num_workers=20)
    
    print("\n")
    input("Press Enter to exit...")
