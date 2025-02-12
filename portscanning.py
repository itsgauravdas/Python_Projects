import socket 
import subprocess
import sys 
import asyncio 
from datetime import datetime 

subprocess.call('cls', shell=True)

# Ask for input 
remoteserver = input('Enter a remote Host to scan:-')
remoteServer = socket.gethostbyname(remoteserver) # get the ip

#Print a nice banner with information on which host we are about to scan 
print('-'*60)
print("Please wait, scanning remote host", remoteServer)
print("-" * 60)

#To get the date 
t1=datetime.now()

async def scan_port(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setblocking(False)
    try:
        await asyncio.wait_for(
            asyncio.get_event_loop().sock_connect(sock,(remoteServer, port)),
            timeout=1
        )
        print("port {}: open".format(port))
    except (socket.timeout,ConnectionRefusedError):
        pass
    finally:
        socket.close()
        
async def main():
    task = []
    for port in range(1,1025):
        task.append(scan_port(port))
    await asyncio.gather(*task)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("You press CTRL+C")
        sys.exit()
    except socket.gaierror:
        print('Host name could not be resolved, Exiting')
        sys.exit()
        
    except socket.error:
        print("Couldn't connect to the server")
        sys.exit()
        
t2=datetime.now()

total =t2-t1

print('Scanning completed in:', total) 



