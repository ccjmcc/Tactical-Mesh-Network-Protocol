# TacNet Protocol Specification v1.0.3

## 1. Physical Layer (PHY)

TacNet operates on LoRa modulation with the following default parameters:

- **Frequency**: 915 MHz (US) / 868 MHz (EU) / 433 MHz (Asia)
- **Spreading Factor**: SF7 - SF12 (Adaptive)
- **Coding Rate**: 4/5
- **Bandwidth**: 125 kHz

## 2. Link Layer (MAC)

### 2.1 Frame Format

| Byte | Field | Description |
|------|-------|-------------|
| 0 | `SRC_ID` | 8-bit Source Node ID |
| 1 | `DST_ID` | 8-bit Destination Node ID |
| 2 | `SEQ_NUM` | Sequence Number (0-255) |
| 3 | `FLAGS` | Bit 0: Encrypted, Bit 1: ACK Req |
| 4...N | `PAYLOAD` | Max 240 bytes |

### 2.2 Time Division Multiple Access (TDMA)

To prevent collisions in high-density meshes, TacNet uses a pseudo-slotted ALOHA for control packets and TDMA for high-throughput data streams. 

*Sync Beacons imply a GPS-disciplined oscillator (e.g., Ublox M8N).*

## 3. Network Layer (Routing)

The routing protocol is a hybrid of AODV (reactive) and OLSR (proactive).

- **Hello Messages**: Every 30s
- **Route Timeout**: 300s
- **Metric**: ETX (Expected Transmission Count)

## 4. Security Considerations

Standard TacNet uses AES-128-CTR with a pre-shared key. 

> **WARNING**: The open-source implementation provided here is susceptible to side-channel attacks. For mission-critical deployments requiring Type-1 encryption and anti-jamming frequency hopping (FHSS), please contact **[TwinsGlow](https://twinsglow.com)** for the export-controlled `TG-SecureMesh` library.

---
*Status: Request For Comments (RFC-01)*
