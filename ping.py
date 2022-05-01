import os, pythonping, socket, time
from pystyle import Write, Colors 
from threading import active_count, Thread

class tool():
    def __init__(self):
        pass

    def title(self, content):
        os.system(f'title {content}')

    def clear(self):
        print("\033c")
        self.main()

    def quit(self):
        for c in range(3, 0, -1):
            Write.Print(f'\n[!] Exiting in {c}', Colors.green_to_white, interval=0.01)
            time.sleep(0.5)
        try:
            exit
        except:
            quit()

    def runDef(self, opt):
        try:
            opt = int(opt)
            #PING        
            if opt == 1:
                ip = Write.Input("\n\n[?] IP > ", Colors.green_to_white, interval=0.01)
                Write.Print("\n[?] Custom packet size?", Colors.green_to_white, interval=0.01)
                Write.Print("\n[!] If 0, packet size will be 1", Colors.green_to_white, interval=0.01)
                buffer = Write.Input("\n[?] Size > ", Colors.green_to_white, interval=0.01)
                try:
                    ip = str(ip)
                    if int(buffer) == 0:
                        buffer = 1
                    else: 
                        buffer = int(buffer)
                    self.ping(ip, buffer)
                except:
                    Write.Print("\n\nValue Error.", Colors.green_to_white, interval=0.01)
                    self.clear()
            
            #PORT SCAN
            elif opt == 2:
                ip = Write.Input("\n\n[?] IP > ", Colors.green_to_white, interval=0.01)
                portrange = Write.Input("\n[?] Port Range (max = 65535) > ", Colors.green_to_white, interval=0.01)
                portrange = int(portrange)
                for port in range(portrange + 1):
                    Thread(target=self.portscan, args=(ip, port)).start()
                    self.title(f'[Scanning port {port}]')
                for c in range(3, 0, -1):
                    Write.Print(f'\n[!] Returning in {c}', Colors.green_to_white, interval=0.01)
                    time.sleep(0.5)
                self.clear()
            #DOS
            elif opt == 3:
                  Write.Print('[!] Unavailable', Colors.green_to_white, interval=0.01)
                  self.clear()
            
            #QUIT
            elif opt == 4:
                self.quit()

            else:
                Write.Print('\n\n[!] Unavailable', Colors.green_to_white, interval=0.01)
                for c in range(3, 0, -1):
                    Write.Print(f'\n[!] Returning in {c}', Colors.green_to_white, interval=0.01)
                    time.sleep(0.5)
                self.clear()
                
        except:
            Write.Print('[!] Value Error', Colors.green_to_white, interval=0.01)
            self.clear()
    
    def ping(self, ip, buffer):
        try:
            while True:
                print(pythonping.ping(ip, verbose=True, size=buffer))
        except:
            pass
    
    #AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses).
    #SOCK_STREAM means that it is a TCP socket. 
    #SOCK_DGRAM means that it is a UDP socket. 
    # These are used 99% of the time.
    def portscan(self, ip, port):
        scanner= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        try:
            scanner.connect((ip, port))
            scanner.close
            Write.Print(f"\n[{port}] > Opened", Colors.green_to_white, interval=0)
        except:
            pass

    def dosatk(self, ip, threads):
        pass

    def main(self):
        self.title('[PING/DOS Tool]')
        Write.Print("""@@@  @@@     @@@@@@@@     @@@  @@@     @@@@@@@@      @@@@@@   
@@@  @@@     @@@@@@@@     @@@@ @@@     @@@@@@@@     @@@@@@@@  
@@!  !@@     @@!          @@!@!@@@          @@!     @@!  @@@  
!@!  @!!     !@!          !@!!@!@!         !@!      !@!  @!@  
@!@@!@!      @!!!:!       @!@ !!@!        @!!       @!@  !@!  
!!@!!!       !!!!!:       !@!  !!!       !!!        !@!  !!!  
!!: :!!      !!:          !!:  !!!      !!:         !!:  !!!  
:!:  !:!     :!:          :!:  !:!     :!:          :!:  !:!  
 ::  :::      :: ::::      ::   ::      :: ::::     ::::: ::  
 :   :::     : :: ::      ::    :      : :: : :      : :  : """, Colors.green_to_white, interval=0)
        Write.Print("\nkxnzx#7093", Colors.green_to_white, interval=0.001)
        Write.Print("\n[1] > Ping\n[2] > Port Scan \n[3] > DOS\n[4] > Quit", Colors.green_to_white, interval=0.01)
        opt = Write.Input("\n[?] > ", Colors.green_to_white, interval=0.01)
        self.runDef(opt)

mainapp = tool()
mainapp.main()