#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MSFV
import WIFI
from os import system

permite = 'N'
while permite == 'N':
    system('\033[32m\033[1m')
    system('clear')
    system('figlet @@@ KHLS @@@')
    print('''$______________________\033[34mVERSÃO 1.0 ANO DE LANÇAMENTO 2019\033[0;0m\033[32m\033[1m___________________$\033[0;0m''')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    impute1 = int(input( '''\033[32m\033[1mESCOLHA UMA OPÇÃO ABAIXO!\033[0;0m
    (1)Gerador de Payload.
    (2)Hacker Wifi.
    (3)Sair!

    \033[32m\033[1mDIGITE UMA OPÇÃO: \033[0;0m'''))
    if impute1 == 1:
        MSFV.Payload_Msfvenon()

    elif imput1 == 2:
        WIFI.Hacker_wireless()

    else:
        print('--------------------------------------------------------------------------')
        print('==================== VOCÊ ESCOLHEU \033[31mSAIR\033[0;0m DO PROGRAMA ======================\n')

    permite = str(input('\033[33mVocê quer mesmo sair do programa\033[0;0m S/N: ')).upper()
    system('clear')
    print('\n$$$$$$$$$$$$$$$$$ \033[33m= Obrigado pela visita =\033[0;0m $$$$$$$$$$$$$$$$$$$$$\n')
    
