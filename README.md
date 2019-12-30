# KHLS-1.0
Ola, bem-vindo ao KHLS essa é a versão 1.0. Esse script foi criado para facilitar a vida de você que gosta ou estuda pentest, principalmente utilizador do Kali linux! Esse escrip só ira funciona se você tiver instalado todas as dependências que ele precisa para  funciona, todos os requisitos necessário tá!Listado-o logo abaixo. O script serve para criar payload, para windows e para androide, ele usa alguns comandos do msfvenom para gera payloads. E também ele ataque em rede wifi com falha no wps ativo, e brute force! Mas lembrando que você vai ter que criar uma wordlist.txt dentro da pasta KHLS-1.0/ para o brute force fusiona OK.      

PREPARO PARA INSTALAÇÃO E INSTALAÇÃO. 

PROGRAMAS NECESSARIO PARA O FUCIONAMENTO DO SCRIP
metasploit-framework 
Aircreck-ng 
reaver 
wash 
figlet   

Para garantir que os repositórios estejam na sua sourcelist.list! Logo abaixo tem instrução de como você pode tá! Fazendo isso OK. Isso funcionara no kali linux. Abra o terminal e digite:  nano etc/apt/sourcelist.list     Agora vai abrir um arquivo parecido com esse abaixo. 

#   

#deb cdrom:[Debian GNU/Linux 2019.3 _Kali-rolling_ - Official Snapshot amd64 LIVE/INSTALL Binary 20190827-12:55]/ kali-last-snapshot contrib main non-free     #deb cdrom:[Debian GNU/Linux 2019.3 _Kali-rolling_ - Oficial Snapshot amd64 LIVE/INSTALL Binary 20190827-12:55]/ kali-last-snapshot contrib main non-free     

deb http://http.kali.org/kali kali-rolling main non-free contrib     

#This system was installed using small removable media # (e.g. netinst, live or single CD). The matching "deb cdrom" # entries were disabled at the end of the installation process. # For information about how to configure apt package sources, # see the sources.list(5) manual.   

Agora cole essas linhas de repositório logo abaixo de deb http://http.kali.org/kali kali-rolling main non-free contrib, e ezeculte o instalador dentro da pasta que você extraiu do arquivo zipado KHLS-1.0-data-28-09-2019.zip que é o KHLS-1.0     

deb http://old.kali.org/kali sana main non-free contrib  
deb http://http.kali.org/kali kali-rolling main contrib non-free  
deb http://old.kali.org/kali moto main non-free contrib   

COMO USAR O KHLS? Primeiramente extraia o arquivo abra o terminal e acesse a pasta com o  comando  abaixo.   

cd KHLS-1.0/ 
chmod 777 install 
./install 

E quando ele termina a instalação, o script vai abrir, e quando você quiser abri-lo, acesse a pasta com os comando abaixo!

cd KHLS-1.0/ 
./khls 
ou acesse 
cd /usr/bin/ 
./khls   

Para o brute force funciona você tem que coloca um dicionário de senhas com o nome de wordlist.txt   E após a instalação ocorrer com sucesso, é só executa o comando khls em qualquer lugar do terminal e dar enter, que o script ira iniciar Para mais informações acesse o nosso canal no youtube LAUDIER ST https://www.youtube.com/channel/UCk8HdZCe8RFMkZqVIQ0mL3g
