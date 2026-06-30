
SEPARADOR = ';'

# ================== SELECOES ============================

#============= Trazer
def carregar_selecoes():
    selecoes = []
    arquivo = open('Banco_de_Dados/selecoes.txt', 'r')

    for linha in arquivo:
        linha = linha.strip()
        if linha == "":
            continue
        selecoes.append(montar_selecao_da_linha(linha))
    arquivo.close()
    return selecoes

def montar_selecao_da_linha(linha):
    partes = linha.split(SEPARADOR)
    selecao = {
        'id': int(partes[0]),
        'nome': partes[1],
        'confederacao': partes[2],
        'grupo': partes[3],
        'ranking_fifa': int(partes[4]),
        'titulos': int(partes[5])
    }
    return selecao

#============== Salvar
def salvar_selecoes(selecoes: list):
    arquivo = open('Banco_de_Dados/selecoes.txt', 'w')

    for s in selecoes:
        linha = montar_linha_selecoes(s)
        arquivo.writelines(linha + '\n')
    arquivo.close()

def montar_linha_selecoes(selecao: list):
    valores = [
        str(selecao['id']),
        selecao['nome'],
        selecao['confederacao'],
        selecao['grupo'],
        str(selecao['ranking_fifa']),
        str(selecao['titulos'])
    ]
    return SEPARADOR.join(valores)

# ================== JOGADORES ============================
#============= Trazer
def carregar_jogadores():
    jogadores = []
    arquivo = open('Banco_de_Dados/jogadores.txt', 'r')

    for linha in arquivo:
        linha = linha.strip()
        if linha == '':
            continue
        jogadores.append(montar_jogador_da_linha(linha))
    arquivo.close()
    return jogadores

def montar_jogador_da_linha(linha):
    partes = linha.split(SEPARADOR)
    jogador = {
        'id': int(partes[0]),
        'nome': partes[1],
        'selecao_id': int(partes[2]),
        'posicao': partes[3],
        'idade': int(partes[4]),
        'gols': int(partes[5])
    }
    return jogador

#============== Salvar
def salvar_jogadores(jogadores: list):
    arquivo = open('Banco_de_Dados/jogadores.txt', 'w')
    for j in jogadores:
        linha = montar_linha_jogadores(j)
        arquivo.writelines(linha + '\n')
    arquivo.close()

def montar_linha_jogadores(jogador: list):
    valores = [
        str(jogador['id']),
        jogador['nome'],
        str(jogador['selecao_id']),
        jogador['posicao'],
        str(jogador['idade']),
        str(jogador['gols'])
    ]
    return SEPARADOR.join(valores)

# ================== PARTIDAS ============================

#============= Trazer
def carregar_partidas():
    partidas = []
    arquivo = open('Banco_de_Dados/partidas.txt', 'r')

    for linha in arquivo:
        linha = linha.strip()
        if linha == '':
            continue
        partidas.append(montar_partida_da_linha(linha))
    arquivo.close()
    return partidas

def montar_partida_da_linha(linha):
    partes = linha.split(SEPARADOR)
    partida = {
        'id': int(partes[0]),
        'selecao_casa_id': int(partes[1]),
        'selecao_fora_id': int(partes[2]),
        'gols_casa': int(partes[3]),
        'gols_fora': int(partes[4]),
        'fase': partes[5]
    }
    return partida

#============== Salvar
def salvar_partidas(partidas: list):
    arquivo = open('Banco_de_Dados/partidas.txt', 'w')

    for p in partidas:
        linha = montar_linha_partidas(p)
        arquivo.writelines(linha + '\n')
    arquivo.close()

def montar_linha_partidas(partida: list):
    valores = [
        str(partida['id']),
        str(partida['selecao_casa_id']),
        str(partida['selecao_fora_id']),
        str(partida['gols_casa']),
        str(partida['gols_fora']),
        partida['fase']
    ]
    return SEPARADOR.join(valores)

# Funcoes genericas =================================================================
def carregar_arquivo(caminho: str):
    itens_do_arquivo = []
    arquivo = open(caminho, 'r')

    for linha in arquivo:
        item = linha.strip()
        if linha == '':
            continue
        
        itens_do_arquivo.append(item)
    return itens_do_arquivo




