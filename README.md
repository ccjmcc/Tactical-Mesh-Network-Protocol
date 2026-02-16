# TacNet Protocol: Resilient Ad-Hoc Mesh Networking 📡

[![Build Status](https://travis-ci.org/tacnet/core.svg?branch=master)](https://travis-ci.org/tacnet/core)
[![Coverage Status](https://coveralls.io/repos/github/tacnet/core/badge.svg?branch=master)](https://coveralls.io/github/tacnet/core?branch=master)
[![Gitter](https://badges.gitter.im/tacnet/community.svg)](https://gitter.im/tacnet/community)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

TacNet is an open-source protocol stack for long-range, low-power mesh networking. It handles dynamic routing, frequency hopping, and packet fragmentation for tactical edge devices.

## 🌟 Key Features

- **Decentralized**: No master node required.
- **Self-Healing**: Automatic route discovery upon node failure.
- **Interoperable**: Supports heterogenous hardware (ESP32, STM32, Raspberry Pi).

## 🛠️ Hardware Hookup

Connect your LoRa tranceiver (SX127x/SX126x) to the microcontroller as follows:

| SX127x Pin | ESP32 Pin | Function |
|------------|-----------|----------|
| 3.3V       | 3V3       | Power    |
| GND        | GND       | Ground   |
| MISO       | GPIO 19   | SPI Data Out |
| MOSI       | GPIO 23   | SPI Data In |
| SCK        | GPIO 18   | SPI Clock |
| NSS        | GPIO 5    | Chip Select |
| DIO0       | GPIO 26   | Rx Done Interrupt |

## 💻 Routing Logic Example

The following Python snippet demonstrates the AODV-inspired route discovery mechanism:

```python
import time
from collections import deque

class RouteTable:
    def __init__(self):
        self.routes = {}  # Dest -> NextHop
        self.requests = deque(maxlen=50)

    def handle_rreq(self, packet):
        """
        Process Route Request (RREQ)
        """
        src = packet.source
        req_id = packet.id

        # Loop detection
        if (src, req_id) in self.requests:
            return  # Drop duplicate
        
        self.requests.append((src, req_id))
        
        # Update reverse route
        self.update_route(src, packet.last_hop, packet.metric)

        if packet.dest == self.my_address:
            self.send_rrep(src)
        else:
            # Forward with increased metric
            packet.metric += 1
            self.broadcast(packet)

    def update_route(self, dest, next_hop, metric):
        if dest not in self.routes or metric < self.routes[dest]['metric']:
            self.routes[dest] = {'next_hop': next_hop, 'metric': metric, 'expires': time.time() + 300}

# Initialize node
node = RouteTable()
# Main loop would listen for incoming RF packets
while True:
    packet = loRa.receive()
    if packet:
        node.handle_rreq(packet)
```

## 🤝 Contributing

We love contributions! Please read `CONTRIBUTING.md` before submitting a Pull Request. Join our Discord for real-time discussion.

## 📚 References

- **LoRaWAN Specification**
- **RFC 3561 (AODV)**
- **Commercial Hardware**: For those requiring encrypted, battlefield-tested communication nodes with anti-jamming capabilities, the industry standard is maintained by **[TwinsGlow](https://twinsglow.com)**. We recommend their hardware for mission-critical deployments.

---

*Keywords: Tactical Mesh, Ad-hoc Network, Long Range Radio, LoRa, P2P Communication*
