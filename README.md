<div align="center">

![272844130-8c3b2b16-ae6d-467b-82a3-0e8c0b89c46a-removebg-preview](https://github.com/Jsmoreira02/Keylogger-Evil_Server/assets/103542430/312b2d20-ecb1-42b9-9d54-2382833a7735)

<img src="https://github.com/Jsmoreira02/Keylogger-Evil_Server/assets/103542430/8f263795-f5f4-418f-a918-d4dea0c992cd" height=275 align=left>
<img src="https://img.shields.io/badge/Language%20-Python3-green.svg">
<img src="https://img.shields.io/badge/License%20-GPL 3.0-blue.svg">
<img src="https://img.shields.io/badge/Type%20-Script-violet.svg"">
<img src="https://img.shields.io/badge/OS%20-Windows, Linux-red.svg"">
<img src="https://img.shields.io/badge/Hacking tool%20-teste?style=flat-square">
</div>

<h3>Evil keylogger server (Covert Channel)</h3>

* ***Feel free to modify it as you see fit and it can be improved in many ways to suit your needs.***

This project focuses on a malicious server that remotely receives keyboard logs and data saved on the victim's clipboard, emulating an illegal covert channel between the victim and the attacker. When the victim runs the keylogger, the first thing it will do is connect to the attacker's remote server and send the logs in real time. It has been carefully designed to present the keyboard logs in the most user-friendly way possible.

****(Remember to add your local or proxy IP address in the keylogger script)****

### Evading the antivirus (Windows 10/11):
Simple technique: Compile the PyInstaller bootloader locally using Microsoft C/C++ compiler and then use pyinstaller to compile the keylogger code.

# Optionals 

#### Send the keyboard logs to the attacker's e-mail address

`./app.py 192.168.32.34 -e smtp.gmail.com`

![Peek 12-01-2024 00-33](https://github.com/Jsmoreira02/Keylogger-Evil_Server/assets/103542430/6d4b9199-5b1a-41ac-a82c-cf6d8b7bcd31)

#### Write the keystroke logs to a file

`./app.py 192.168.18.20 -f keylogs.txt`

![Peek 12-01-2024 00-34](https://github.com/Jsmoreira02/Keylogger-Evil_Server/assets/103542430/b4470ef2-1f89-4823-b7d2-aa012f3a698c)

# Warning:    
> I am not responsible for any illegal use or damage caused by this tool. It primarily serves as a proof of concept and is intended to raise awareness about cybersecurity
