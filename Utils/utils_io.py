import os


# Geral =================================================================
def limpar_tela():
    os.system('cls')

def sucesso():
    print(f'\nOperacao realizada com sucesso.')

def obter_opcao(menu, lim_inferior: int, lim_superior: int):
    opcao = obter_inteiro_faixa(menu, lim_inferior, lim_superior)
    return opcao

def obter_grupo(prompt: str):
    grupos_validos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    while True: 
        grupo = obter_texto(prompt).upper()
        if grupo in grupos_validos:
            return grupo
        else:
            limpar_tela()
            print(f'\n\t\tATENCAO: | O VALOR DIGITADO NAO E UM GRUPO VALIDO! |')
            print(f'\n\tVerifique se existem selecoes cadastradas com este grupo e tente novamente.')

def obter_atributos(prompt: str, atributos_validos: list):
    while True: 
        atributo = obter_texto(prompt).lower()
        atributo = atributo.replace(' ', '_')
        if atributo in atributos_validos:
            return atributo
        else:
            limpar_tela()
            print(f'\n\t\tATENCAO: | O VALOR DIGITADO NAO E UM ATRIBUTO VALIDO! |')
            print(f'\n\tVerifique se o atributo esta entre as opcoes ou se ha algum erro de ortografia e tente novamente.')
    
# Strings ===============================================================
def obter_texto(prompt: str):
    texto = input(prompt)
    return texto

# Inteiros ==============================================================
def obter_inteiro(prompt:str):
    while True:
        try:
            numero = int(input(prompt))
            return numero
        except:
            limpar_tela()
            print(f'\n\tATENCAO: VALOR INVALIDO. | O valor digitado nao e um numero inteiro!')

def obter_inteiro_positivo(prompt:str):
    while True:
        numero = obter_inteiro(prompt)
        if numero >= 0:
            return numero
        else:
            limpar_tela()
            print(f'\n\tATENCAO: VALOR INVALIDO. | O valor digitado nao e positivo!')

def obter_inteiro_faixa(prompt: str, lim_inferior: int, lim_superior: int):
    while True:
        numero = obter_inteiro(prompt)
        if numero >= lim_inferior and numero <= lim_superior:
            return numero
        else:
            limpar_tela()
            print('\nATENCAO: OPCAO INVALIDA | O valor digitado nao esta entre as opcoes validas!')

# Floats ==================================================
def obter_float(prompt: str):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except:
            print(f'\n\tATENCAO: VALOR INVALIDO. | O valor digitado nao e um numero decimal!')