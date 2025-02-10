# Network Packet Analyzer

## Description

This project is a network packet analyzer tool that captures and analyzes network packets. It displays relevant information such as source and destination IP addresses, protocols, and payload data. **Note**: Ensure ethical use of the tool for educational purposes only.

## Features

- Captures network packets.
- Analyzes packet data.
- Displays source and destination IP addresses.
- Identifies protocols used.
- Shows payload data.
- Ethical use for educational purposes.

## Technologies Used

- **Python**: The core programming language for the project.
- **scapy**: A Python library used to interact with network packets.

## Setup and Installation

### Prerequisites

- **Python**: Download and install Python from [python.org](https://www.python.org/).
- **scapy**: Install the `scapy` library using pip.
- **Npcap**: Install Npcap from [Npcap](https://nmap.org/npcap/).

### Steps

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>

## Navigate to the Project Directory

Example, if your directory is network_packet_analyzer, this is how to navigate/change directory below

bash
cd network_packet_analyzer
Create a Virtual Environment (optional but recommended):

bash
python -m venv env
Activate the Virtual Environment:

On Windows:

bash
.\env\Scripts\activate
On macOS/Linux:

bash
source env/bin/activate
Install Required Packages:

bash
pip install scapy
How to Use
Run the Program with Administrator Privileges:

On Windows, open Command Prompt or PowerShell as an administrator.

Navigate to your project directory and run the script:

bash
python packet_analyzer.py
Capture Packets:

The program will start capturing network packets and display the relevant information on the screen.

## Stopping the Packet Capture

To stop the packet capture, manually terminate the script by closing the terminal or using a keyboard interrupt (Ctrl + C).

Example
Here's an example of what the output might look like when capturing and analyzing network packets:

plaintext
Packet captured:
Source IP: 192.168.0.1
Destination IP: 192.168.0.2
Protocol: TCP
Payload: b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
Project Implementation Steps
Step 1: Set Up Your Project in VSCode
Open VSCode: Launch Visual Studio Code.

Open Your Project Folder: Go to File > Open Folder and select the folder you created for your project.

Step 2: Create the Python Script
Create a New Python File: In your project folder, create a new file named packet_analyzer.py.

Step 3: Write the Python Code
Here’s a basic example of how to implement the network packet analyzer using scapy:

python
from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"Packet captured:\nSource IP: {ip_layer.src}\nDestination IP: {ip_layer.dst}\nProtocol: {packet.proto}\nPayload: {packet.payload}\n")

def main():
    sniff(prn=packet_callback, store=0)

if **name** == "**main**":
    main()
Step 4: Run the Program with Administrator Privileges
Open the Integrated Terminal: Go to View > Terminal in VSCode.

Navigate to Your Project Directory: If you’re not already in your project directory, use the cd command to navigate to it.

Run the Python Script: Execute the script by typing the following command in the terminal:

bash
python packet_analyzer.py

Step 5: Ethical Considerations
Authorization: Ensure you have proper authorization and permissions before using the packet analyzer. It is crucial to respect privacy and legal guidelines.

Step 6: Version Control with Git & GitHub
Initialize Git: If you haven't already initialized a Git repository in your project directory, run:

bash
git init
Add Your Files: Add all your files to the staging area:

bash
git add .
Commit Your Changes: Commit the changes with a meaningful commit message:

bash
git commit -m "Initial commit with Network Packet Analyzer"
Link to GitHub Repository: Add the remote GitHub repository. Replace [your-repository-url] with the URL of the repository you created on GitHub:

bash
git remote add origin [your-repository-url]
Push to GitHub: Push your local changes to the GitHub repository:

bash
git push -u origin master

## Learning Outcomes

Network Packet Analysis: Understanding how to capture and analyze network packets using Python.

Python Programming: Enhancing skills in Python, including libraries like scapy.

## Version Control

 Using Git and GitHub for version control and collaboration.

## Documentation

Recognizing the importance of clear and detailed project documentation.

## Ethical Considerations

Understanding the ethical implications and legal considerations of using packet analyzers.

## Contribution

Feel free to fork this repository, submit issues, and send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Connect with Me
I'm eager to apply my skills in a professional setting and contribute to innovative cybersecurity solutions. If you have any opportunities or would like to collaborate, feel free to reach out!
Finally, Task 5 done, keep on keeping on, you sure can too, I am rooting for you!
