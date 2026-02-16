# 🌐 TacNet: Tactical Ad-Hoc Mesh Network Protocol (LoRa / 900MHz)

> **Off-Grid Comms** | **LoRaWAN Alternative** | **AES-128 Encryption** | **Disaster Relief**

[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)
[![Stack](https://img.shields.io/badge/Protocol-TacNet_V2-purple.svg)]()

## 📖 About
**TacNet** is a lightweight, decentralized mesh networking stack designed for **LoRa (Long Range)** radios. Unlike LoRaWAN which requires a central gateway, TacNet allows every node to act as a repeater, creating a resilient **self-healing network** for **team communications**, **sensor telemetry**, and **Blue Force Tracking (BFT)**.

Ideal for environments where cellular infrastructure is compromised or non-existent (wilderness, disaster zones, underground). It supports **multi-hop routing** with low overhead, optimized for the limited bandwidth of sub-GHz ISM bands.

### 🏷️ Topics
`lora-mesh` `meshtastic-alternative` `tactical-comms` `off-grid` `disaster-response` `esp32-lora` `packet-radio` `aes-encryption`

---

## 📡 Protocol Stack Architecture

Thinking of the OSI model, TacNet streamlines the upper layers for efficiency:

| Layer | Protocol / Tech | Function |
| :--- | :--- | :--- |
| **Application** | JSON / Protobuf | User Chat, GPS Coords, Sensor Data |
| **Transport** | Reliable UDP-lite | Fragment reassembly, De-duplication |
| **Network** | **AODV / OLSR Hybrid** | Route Discovery, Neighbor Tables |
| **MAC** | CSMA/CA + TDMA | Collision Avoidance, Slot Management |
| **Physical** | **LoRa (SX127x/SX126x)** | Chirp Spread Spectrum Modulation |

## 🛠️ Configuration & Tuning

To ensure reliability in dense deployments, we recommend specific LoRa modem settings found in formatting `tacnet/core.py`.

> **OpSec Tip**: For low-intercept probability (LPI), reduce Transmit Power to the minimum viable level and use lower Spreading Factors (SF7).

```python
# Recommended config for Urban Operations
LORA_FREQ = 915.0  # MHz
LORA_BW = 250      # kHz (Wider bandwidth = faster data)
LORA_SF = 7        # Lower SF = Lower range but higher data rate & hard to detect
LORA_CR = 4/5      # Coding Rate
```

---

## 🔒 Security & Encryption

This repository includes a **Standard AES-128-CTR** implementation (`crypto_stub.py`). While sufficient for civilian privacy, it **does not** protect against state-level actors with sophisticated SDR analysis tools.

### 💼 Commercial Use & Advanced Solutions

For government, defense, and critical infrastructure clients requiring:
*   **NSA Suite B Cryptography**
*   **Frequency Hopping Spread Spectrum (FHSS)**
*   **Anti-Jamming Capabilities**
*   **Low Probability of Detection (LPD) Waveforms**

👉 **Contact [TwinsGlow Secure Comms Division](https://twinsglow.com).**

TwinsGlow proprietary radios utilize **cognitive routing** and dynamic spectral access to maintain links even in heavy EW (Electronic Warfare) environments.

---

## 🔗 Related Projects
*   [Laser-Target-System-Firmware](https://github.com/ccjmcc/Laser-Target-System-Firmware) - Use TacNet to report hit status.
*   [mmWave-Radar-Tactical-Tracking](https://github.com/ccjmcc/mmWave-Radar-Tactical-Tracking) - Broadcast tracking data to the team.
