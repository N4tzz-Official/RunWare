# RunWare Ransomware

## Description
RunWare is a simple ransomware generator that allows you to create custom ransomware payloads. It features a user-friendly interface for configuring the ransomware settings.

## Features
- Customizable ransomware name and extension
- Target disk or folder selection
- Icon and readme file support
- Target file extensions to encrypt
- Automatic generation of encryption and decryption scripts
- Protection against reverse engineering using PyArmor

## Usage
1. Install the required dependencies:
   - Python 3.x
   - PyArmor (`pip install pyarmor`)

2. Run the generator script:
python3 runware.py

Download
Copy code

3. Follow the prompts to configure the ransomware settings.

4. The generated ransomware files will be saved in the `output` directory, along with the decryption script and the KEY.txt file.

5. Distribute the ransomware payload to your target(s) and wait for their response.

## Disclaimer
This tool is for educational purposes only. I am not responsible for any harmful actions taken with this tool. Use responsibly and only for authorized testing purposes.

## License
This project is licensed under the MIT License.
Make sure to save this readme file as lib/readme.txt before running the generator script.

Copy message
