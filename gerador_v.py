#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MSFV
import WIFI
import os

rl = 'N'
while rl == 'N':
    os.system('\033[32m\033[1m')
    os.system('clear')
    os.system('figlet @@@ KHLS @@@')
    print('''$______________________\033[34mVERSÃO 1.0 ANO DE LANÇAMENTO 2019\033[0;0m\033[32m\033[1m___________________$\033[0;0m''')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    d = int(input( '''\033[32m\033[1mESCOLHA UMA OPÇÃO ABAIXO!\033[0;0m
    (1)Gerador de Payload.
    (2)Hacker Wifi.
    (3)Sair!

    \033[32m\033[1mDIGITE UMA OPÇÃO: \033[0;0m'''))
    if d == 1:
        MSFV.Payload_Msfvenon()

    elif d == 2:
        WIFI.Hacker_wireless()

    else:
        print('--------------------------------------------------------------------------')
        print('==================== VOCÊ ESCOLHEU \033[31mSAIR\033[0;0m DO PROGRAMA ======================\n')

    rl = str(input('\033[33mVocê quer mesmo sair do programa\033[0;0m S/N: ')).upper()
    print('\n$$$$$$$$$$$$$$$$$ \033[33mObrigado pela visita, volte sempre\033[0;0m $$$$$$$$$$$$$$$$$$$$$\n')
