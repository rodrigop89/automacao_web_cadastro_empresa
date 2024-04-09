# Aplicativo de execução do sistema

import os
import signal
import sys
import time

from sistema import abre_navegador, login, preencher_planilha

# Função para lidar com o sinal de interrupção (Ctrl+C)


def signal_handler(sig, frame):
    print('Encerrando o programa...')
    sys.exit(0)


# Configurando o handler para o sinal de interrupção
signal.signal(signal.SIGINT, signal_handler)

# Mensagem de aviso de inicio do programa
print("Iniciando o programa, aguarde...")

if os.path.exists('empresas.xlsx'):
    # Se o arquivo existir, faça o que precisa ser feito
    # Por exemplo, você pode abrir o arquivo aqui
    with open('empresas.xlsx', 'r') as file:
        # Faça algo com o arquivo
        pass
else:
    # Se o arquivo não existir, imprima uma mensagem de erro
    print("Planilha não encontrado.")

# 1. Abre o navegador Chrome e acessa o site
abre_navegador()
# 2. Faz o login
login()
# 3. Preenche os dados de acordo com a planilha, salva o cadastro e aguarda para prosseguir para o próximo
preencher_planilha()
time.sleep(4)
