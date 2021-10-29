import threading
import colorama
from colorama import Fore
import requests
import time

print("              ____              _           _____ ")                                          
print("             |  _ \            | |         / ____|")                                          
print("             | |_) | __ _ _ __ | | _____  | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ ") 
print("             |  _ < / _` | '_ \| |/ / __|  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|") 
print("             | |_) | (_| | | | |   <\__ \  ____) | |_) | (_| | | | | | | | | | | |  __/ |  ")  
print("             |____/ \__,_|_| |_|_|\_\___/ |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   ") 
print("                                                 | |                                        ") 
print("                                                 |_|                                        ") 



print("                                      Made by Banks#6485")
channel = input('Id of channel: ')
mess = input('Message to spam: ')
delay = input('Delay: ')

tokens = open("tokens.txt", "r").read().splitlines()


def spam(token, channel, mess):
    url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
    data = {"content": mess}
    header = {"authorization": token}

    while True:
        time.sleep(int(delay))
        r = requests.post(url, data=data, headers=header)
        print(r.status_code)



def thread():
    channel_id = channel
    text = mess
    for token in tokens:
        time.sleep(int(delay))
        threading.Thread(target=spam, args=(token, channel_id, text)).start()


start = input('Press eny key when you will be ready ')
start = thread()
