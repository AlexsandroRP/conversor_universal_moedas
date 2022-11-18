### IMPORTAÇÃO DAS BIBLIOTECAS NECESSÁRIAS ###
import requests
import json

### DEFINIÇÃO DAS FUNÇÕES ###
def bem_vindo():
    print("-"*43)
    print("BEM VINDO AO CONVERSOR DE MOEDAS UNIVERSAL!")
    print("-"*43)

def opcao_menu(moeda):
    if moeda == '1':
        moeda = 'USD'
    elif moeda == '2':
        moeda = 'BRL'
    elif moeda == '3':
        moeda = input("Digite o código de 3 digitos da moeda: ").upper()
    return moeda      

def verificar_moeda_selecionada(mensagem):
    escolha_errada = True
    while escolha_errada:
        moeda_usuario = input('[1] - USD\n[2] - BRL\n[3] - Outra\nEscolha a moeda desejada: ')
        if moeda_usuario not in ('1','2','3'):
            print("ERRO. Digite um dos valores do menu!")
            escolha_errada = True
        else:
            return moeda_usuario   

def escolha_moeda_um():
    moeda_usuario = verificar_moeda_selecionada("Escolha a primeira moeda:")  
    moeda_um = opcao_menu(moeda_usuario)
    return moeda_um

def escolha_moeda_dois():
    moeda_usuario = verificar_moeda_selecionada("Escolha a segunda moeda:")  
    moeda_dois = opcao_menu(moeda_usuario)
    return moeda_dois               

def requisicao_moedas(moeda_um, moeda_dois):
    requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{moeda_um}-{moeda_dois}')
    requisicao_json = requisicao.json()
    valor_moeda_atual = float(requisicao_json[f'{moeda_um}{moeda_dois}']['bid'])
    print(f'1 {moeda_um} = {valor_moeda_atual:,.2f} {moeda_dois}')
    return valor_moeda_atual


def calcular_conversao_moedas(valor_escolhido):
    valor_a_converter = float(input("Digite um valor a ser convertido: "))
    conversao = float(valor_escolhido * valor_a_converter)
    
    print(f'RESULTADO: {primeira_moeda_usuario} {valor_a_converter:,.2f} = {segunda_moeda_usuario} {conversao:,.2f}')

def continuar_parar():
    escolha = input("Deseja continuar o programa? s/n: ").lower()
    if 's' in escolha:
        return True    
    elif 'n' in escolha:
        print("-"*20)
        print("PROGRAMA FINALIZADO")
        print("-"*20)
        return False
    return escolha            


### APP PRINCIPAL ###
bem_vindo()
programa_rodando = True

while programa_rodando:
    primeira_moeda_usuario = escolha_moeda_um()
    segunda_moeda_usuario = escolha_moeda_dois()
    
    valores_escolha = requisicao_moedas(primeira_moeda_usuario, segunda_moeda_usuario)
    calcular_conversao_moedas(valores_escolha)
    programa_rodando = continuar_parar()
    
    
    
