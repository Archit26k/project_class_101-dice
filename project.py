import random

response = 'r'

while response == 'r':
    response = input('To roll a dice press r or to exit press e')
    no = random.randint(1,6)
    if(no == 1):
        print('[⇷⇷⇹⇸⇸]')
        print('[⇷⇷⇹⇸⇸]')
        print('[  ⦿  ]')
        print('[⇷⇷⇹⇸⇸]')
        print('[⇷⇷⇹⇸⇸]')
    elif(no == 2):
        print('[⇷⇷⇹⇸⇸]')
        print('[⇷⇷⇹⇸⇸]')
        print('[ ⦿ ⦿ ]')
        print('[⇷⇷⇹⇸⇸]')
        print('[⇷⇷⇹⇸⇸]')     
    elif(no == 3):
        print('[⇷⇷⇹⇸⇸]')
        print('[  ⦿  ]')
        print('[  ⦿  ]')
        print('[  ⦿  ]')
        print('[⇷⇷⇹⇸⇸]')    
    elif(no == 4):
        print('[⇷⇷⇹⇸⇸]')
        print('[ ⦿ ⦿ ]')
        print('[     ]')
        print('[ ⦿ ⦿ ]')
        print('[⇷⇷⇹⇸⇸]') 
    elif(no == 5):
        print('[⇷⇷⇹⇸⇸]')
        print('[ ⦿ ⦿ ]')
        print('[ ⦿   ]')
        print('[ ⦿ ⦿ ]')
        print('[⇷⇷⇹⇸⇸]')   
    elif(no == 6):
        print('[⇷⇷⇹⇸⇸]')
        print('[ ⦿ ⦿ ]')
        print('[ ⦿ ⦿ ]')
        print('[ ⦿ ⦿ ]')
        print('[⇷⇷⇹⇸⇸]')                             
    if(response == 'e'):
        break