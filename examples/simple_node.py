import sys
import time
from tacnet.core import TacNode

def main():
    print("Initializing Tactical Mesh Node...")
    # Simulate Node ID 4
    node = TacNode(node_id=4)
    
    print("Waiting for network convergence...")
    time.sleep(1)
    
    # Try sending telemetry
    target = 1 # Commander Node
    payload = "GPS:34.0522,-118.2437"
    
    success = node.send_packet(target, payload)
    if not success:
        print("Route not found. Retrying discovery...")

if __name__ == "__main__":
    main()
