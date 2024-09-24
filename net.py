import streamlit as st
from scapy.all import sniff, IP, TCP, UDP, ICMP

# Streamlit UI
st.title("Simple Network Traffic Analyzer")

# Number of packets to capture
num_packets = st.number_input("Number of packets to capture", 1, 100)

# Start capture button
if st.button("Start Capture"):
    st.write(f"Capturing {num_packets} packets...")

    # Initialize a packet counter
    packet_counter = 1

    # Function to capture and display packets
    def capture_packet(packet):
        global packet_counter
        if IP in packet:  # Check if the packet has an IP layer
            protocol = "Other"
            if TCP in packet:
                protocol = "TCP"
            elif UDP in packet:
                protocol = "UDP"
            elif ICMP in packet:
                protocol = "ICMP"

            # Display packet details in the desired format
            st.write(f"Packet {packet_counter}:")
            st.write(f"- Source IP: {packet[IP].src}")
            st.write(f"- Destination IP: {packet[IP].dst}")
            st.write(f"- Protocol: {protocol}")
            st.write(f"- Size: {len(packet)} bytes\n")

            # Increment the packet counter
            packet_counter += 1

    # Capture the packets
    sniff(count=num_packets, prn=capture_packet)
