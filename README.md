
---

# Simple Network Traffic Analyzer

This project is a lightweight network traffic analyzer built using **Python**, **Scapy**, and **Streamlit**. It allows users to capture a specified number of network packets and displays basic information like **Source IP**, **Destination IP**, and **Packet Size**.

## Features

- **Real-Time Network Traffic Capture**: Capture live network packets.
- **Basic Packet Information**: Displays source IP, destination IP, and packet size in bytes.
- **User-Friendly Interface**: Built with Streamlit for an easy-to-use web-based UI.
- **Customizable Packet Count**: Select how many packets to capture with a simple slider.

## How It Works

1. **Capture Network Packets**: The app uses Scapy to capture live network packets from your system.
2. **Display Packet Information**: For each packet, the app shows:
   - **Source IP**: The IP address where the packet originated.
   - **Destination IP**: The IP address the packet is heading to.
   - **Packet Size**: The size of the packet in bytes.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/simple-network-traffic-analyzer.git
   cd simple-network-traffic-analyzer
   ```

2. Install the required dependencies:

   ```bash
   pip install streamlit scapy
   ```

## Running the App

To run the app, use the following command:

```bash
sudo streamlit run simple_network_analyzer.py
```

> **Note**: Running the app requires root or administrative privileges to capture network packets.

## How to Use

1. After running the command, the app will open in your default web browser.
2. Select the number of packets you want to capture using the **slider**.
3. Click the **"Start Capture"** button to begin capturing live network traffic.
4. View the details of each captured packet (Source IP, Destination IP, and Size).

## Example

After capturing, the app will display output like:

```
Packet 1:
- Source IP: 192.168.1.101
- Destination IP: 172.217.16.174
- Protocol: TCP
- Size: 66 bytes

Packet 2:
- Source IP: 192.168.1.101
- Destination IP: 151.101.1.69
- Protocol: TCP
- Size: 52 bytes

```

## Requirements

- **Python 3.x**
- **Streamlit**: For the web interface.
- **Scapy**: For capturing and analyzing network packets.

You can install the requirements using:

```bash
pip install -r requirements.txt
```

### Summary

- **Features**: Simple, user-friendly traffic capture with Streamlit.
- **Setup**: Clone the repo, install dependencies, and run the app.
- **Use Case**: Great for learning basic network traffic analysis in Python!

---
