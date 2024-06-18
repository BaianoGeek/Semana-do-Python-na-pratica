import yfinance
from time import sleep
import pyautogui
import pyperclip

ticker = ["BTC-USD", "ETH-USD", "COTI-USD", "SOL-USD", "AVAX-USD"]
valorFechamento = {}

#Solicitação de valores ao usuário
inicial = input("Digite a data inicial(Ex:2024-06-17): ")
final   = input("Digite a data final(Ex:2024-06-17): ")

#Loop
for cripto in ticker:
    dados = yfinance.Ticker(cripto)
    tabela = dados.history(start=inicial, end=final)

    fechamento = tabela.Close
    valorArredondado = round(fechamento, 3)
    for valor in valorArredondado:
        valorFechamento[cripto] = valor

#Recebimento de valores nas variaveis
btc  = valorFechamento["BTC-USD"]
eth  = valorFechamento["ETH-USD"]
coti = valorFechamento["COTI-USD"]
sol  = valorFechamento["SOL-USD"]
avax = valorFechamento["AVAX-USD"]

#Contato que seá enviado a mensagem no WhatsApp
contato = {"contato1", "contato2"}

#Mensagem
mensagem = f"""
Olá, boa tarde!

Abaixo, segue cotações do dia:

Bitcoin  = {btc}
Etherium = {eth}
Coti     = {coti}
Solana   = {sol}
Avax     = {avax}
"""

#Abrir WhatsApp
pyautogui.PAUSE = 3
pyautogui.click(x=3474, y=1063)

for contatos in contato:
    #Clicar em Barra de pesquisa
    pyautogui.PAUSE = 2
    pyautogui.click(x=2132, y=125)
    pyperclip.copy(contatos)
    pyautogui.hotkey("ctrl", "v")

    #clique no contato
    pyautogui.PAUSE = 3
    pyautogui.click(x=2272, y=188)

    #Clique no campo mensagem
    pyautogui.PAUSE = 3
    pyautogui.click(x=2650, y=1006)
    pyperclip.copy(mensagem)
    pyautogui.hotkey("ctrl", "v")

    #Enviar
    pyautogui.PAUSE = 2
    pyautogui.click(x=3805, y=1010)
