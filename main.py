import dns.resolver
import os
import requests
import time
import socket


class find:

    def find_domain(url, wordlist):
        found_newurl = []
        try:
            with open(wordlist, "r") as file:
                for line in file:
                    domain = line.replace('\n', '')
                    newurl = url + domain
                    searching = requests.get(newurl)
                    if searching.status_code == 200:
                        print(f"Found: {newurl}")
                        found_newurl.append(newurl)
                    else: print(f'Not Found: {newurl}')
        except Exception as error:
            print(f"An error occurred: {error}")

    def find_subdomain(url, wordlist_sub):
        found_subdomain = []
        with open(wordlist_sub, "r") as file:
            for line in file:
                subdomain = line.replace('\n','')
                newurl = url.replace('http://', f'http://{subdomain}.')
                try:
                    dns.resolver.resolve(newurl) #realiza requisicao de subdominio
                    print(f"Found: {newurl}")
                    found_subdomain.append(newurl)
                except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                    pass
            clear_console = str(input('Clear console? (Y/N)')).isalpha.upper()
            if clear_console in ["Y", "YES"]:
                os.system('clear || cls')
            print('\nTotal found subdomains:\n')
            for i in found_subdomain:
                print(i)

    def teste_arg(enderecoIP):
        for portas in range(1,3001):
            resultado = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if resultado.connect_ex((enderecoIP, portas)) == 0:
                print(f'Porta {portas} aberta!')
                resultado.close()
            else: print(f'Porta {portas} fechada!')

os.system('cls || clear')

while True:
    option = int(input(f"{'-'*20} \nWelcome to scanner Sub_Domain!!\nWhat u want to scan?\n1) Domain.\n2) Subdomain.\n3) Scanner Port.\n{'-'*20}\nOption: "))

    match option:

        case 1: #chama função de dominio
            url = str(input("URL: "))
            wordlist = str(input("Wordlist path (press ENTER to pass): "))
            find.find_domain(url, wordlist)
    
        case 2: #chama funcao de subdominio
            url = str(input("URL: "))
            wordlist = str(input("Wordlist path (press ENTER to pass): "))
            find.find_subdomain(url, wordlist)

        case 3:
            enderecoIP = input('Insira o ip: ')
            find.teste_arg(enderecoIP)

        case _: #opcao invalida
            print("\nInvalid option, try again in few seconds... \n")
            time.sleep(6)
            os.system('clear || cls')