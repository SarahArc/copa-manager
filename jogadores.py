from rich.console import Console
from rich.table import Table

from debbug import printar_elementos_in_list
from Utils.utils import ordenar_lista_asc_desc, filtrar_por_atributo_ou_sigla, filtrar_por_valor_do_atributo, formar_str_separada_por_virgula, trazer_id_por_nome, trazer_nome_selecao_por_id
from Utils.utils_io import limpar_tela, obter_texto

console = Console()

# Opcao 5 =======================================================================
def cadastrar_jogador(selecao: str, posicao: str, nome_do_jogador: str, idade: int, gols: int, selecoes: list, jogadores: list):
    id_selecao = trazer_id_por_nome(selecao, selecoes)
    id_jogador = criar_id_jogador(jogadores)

    novo_jogador = {'id': id_jogador, 'nome': nome_do_jogador, 'selecao_id': id_selecao, 'posicao': posicao, 'idade': idade, 'gols': gols}
    jogadores.append(novo_jogador)
    return jogadores

def criar_id_jogador(jogadores: list):
    id = 100 + len(jogadores)
    return id


# Opcao 6 =======================================================================
def listar_jogadores(titulo_da_tabela: str, jogadores: list):
    exibir_tabela_jogadores_bonita(titulo_da_tabela, jogadores)

def organizar_jogadores(atributo: str, ordem: int, selecoes: list, jogadores: list):
    for s in selecoes:
        lista_de_jogadores = []
        for j in jogadores:
            nome_selecao = trazer_nome_selecao_por_id(selecoes, j, 'selecao_id')
            j['nome_selecao'] = nome_selecao
            lista_de_jogadores.append(j)
        if lista_de_jogadores != []:
            lista_de_jogadores = ordenar_lista_asc_desc(atributo, lista_de_jogadores, ordem)
            return lista_de_jogadores

def ordenar_jogadores_por_atributo(atributo: str, ordem: int, jogadores:list):
    if ordem == 1:
        jogadores = sorted(jogadores, key=lambda jogador: jogador[atributo])
        return jogadores
    elif ordem == 2:
        jogadores = sorted(jogadores, key=lambda jogador: jogador[atributo], reverse=True)
        return jogadores
    
def exibir_tabela_jogadores_bonita(titulo_tabela: str, lista_dos_jogadores: list):
        limpar_tela()
        tabela = Table(title=titulo_tabela)
        tabela.add_column("ID", justify="right", style="cyan")
        tabela.add_column("Nome", style="bold")
        tabela.add_column("Selecao", justify="center")
        tabela.add_column("Posicao", justify="center")
        tabela.add_column("Idade", justify="right", style="green")
        tabela.add_column("N de Gols", justify="right", style="green")
        for jogador in lista_dos_jogadores:
            tabela.add_row(str(jogador["id"]), jogador["nome"], jogador["nome_selecao"], jogador["posicao"], str(jogador["idade"]), str(jogador["gols"]))
        console.print(tabela)
        
# Opcao 7 =======================================================================
def listar_jogadores_filtrados(titulo_tabela: str, selecoes: list, jogadores: list):
    nova_lista = trazer_nome_selecao_por_id_lista(selecoes, jogadores)
    exibir_tabela_jogadores_filtrados(titulo_tabela, nova_lista)

def filtrar_jogadores(atributo: str, valor_digitado: str, jogadores: list):
    jogadores_filtrados = filtrar_por_atributo_ou_sigla(valor_digitado, atributo, jogadores)
    return jogadores_filtrados

def tratar_valor_digitado(valor: str):
    while True:
        try:
            valor_tratado = int(valor)
            return valor_tratado
        except:
            return valor

def trazer_nome_selecao_por_id_lista(selecoes: list, jogadores: list):
    for s in selecoes:
        lista_de_jogadores = []
        for j in jogadores:
            nome_selecao = trazer_nome_selecao_por_id(selecoes, j, 'selecao_id')
            j['nome_selecao'] = nome_selecao
            lista_de_jogadores.append(j)
        return lista_de_jogadores


def exibir_tabela_jogadores_filtrados(titulo_tabela: str, jogadores_filtrados: list):
        limpar_tela()
        if jogadores_filtrados == None or jogadores_filtrados == []:
            limpar_tela()
            print(f'\n\t{titulo_tabela}\n\tAte o momento ainda nao ha jogadores cadastrados com este parametro.')
        else:
            limpar_tela()
            tabela = Table(title=titulo_tabela)
            tabela.add_column("ID", justify="right", style="cyan")
            tabela.add_column("Nome", style="bold")
            tabela.add_column("Selecao", justify="center")
            tabela.add_column("Posicao", justify="center")
            tabela.add_column("Idade", justify="right", style="green")
            tabela.add_column("N de Gols", justify="right", style="green")
            for jogador in jogadores_filtrados:
                tabela.add_row(str(jogador["id"]), jogador["nome"], jogador["nome_selecao"], jogador["posicao"], str(jogador["idade"]), str(jogador["gols"]))
            console.print(tabela)
# Opcao 8 =======================================================================
def estatisticas(selecao: str, selecoes: list, jogadores: list):
    jogadores_da_selecao = filtrar_jogadores_da_selecao(selecao, selecoes, jogadores)
    qtd_jogadores = len(jogadores_da_selecao)
    if qtd_jogadores == 0:
        print(f'\nAinda nao ha jogadores cadastrados nesta selecao.')
    else:
        gols_do_elenco = calcular_gols_elenco(jogadores_da_selecao)
        media_idade = calcular_media_idade(jogadores_da_selecao, qtd_jogadores)

        print(f' - Total de jogadores: {qtd_jogadores}')
        print(f' - Total de gols do elenco: {gols_do_elenco}')
        print(f' - Media de idade: {media_idade}')
        atacantes = filtrar_atacantes_com_mais_de2_gols(jogadores_da_selecao)
        if atacantes == None:
            atacantes = f'Ainda nao ha atacantes com mais de 2 gols nesta selecao.'
        else:
            atacantes = formar_str_separada_por_virgula(atacantes)
            print(f' - Atacantes com +2 gols: {atacantes}')
            print(f'\nArtilheiro da copa: ', artilheiro_da_copa(jogadores, selecoes))

def artilheiro_da_copa(jogadores: list, selecoes: list):
    artilheiro = filtrar_atacante_com_mais_gols(jogadores)
    selecao = trazer_nome_selecao_por_id(selecoes, artilheiro, 'selecao_id')
    mensagem = f'{artilheiro['nome']} ({selecao}) - {artilheiro['gols']} gols'
    return mensagem

def filtrar_atacante_com_mais_gols(jogadores: list):
    atacante = filtrar_atacantes(jogadores)
    if atacante != None:
        index_jogador = 0
        for j in jogadores:
            if index_jogador == 0:
                atacante_com_mais_gols = j
            if j['gols'] > atacante_com_mais_gols['gols']:
                atacante_com_mais_gols = j
            index_jogador += 1
    return atacante_com_mais_gols

def filtrar_atacantes_com_mais_de2_gols(jogadores: list):
    atacantes_filtrados = []
    atacantes = filtrar_atacantes(jogadores)
    if atacantes != None:
        for jogador in atacantes:
            if jogador['gols'] > 2:
                atacantes_filtrados.append(jogador)
        return atacantes_filtrados
    else:
        None

def filtrar_atacantes(jogadores_da_selecao: list):
    atacantes = filtrar_por_valor_do_atributo('posicao', 'Atacante', jogadores_da_selecao)
    return atacantes

def calcular_media_idade(jogadores: list, qtd_jogadores: int):
    somatorio_idade = 0
    for j in jogadores:
        somatorio_idade += j['idade']
    media_idade = somatorio_idade / qtd_jogadores
    return media_idade

def calcular_gols_elenco(jogadores: list):
    somatorio_gols = 0
    for j in jogadores:
        somatorio_gols += j['gols']
    return somatorio_gols

def filtrar_jogadores_da_selecao(selecao: str, selecoes: list, jogadores: list):
    jogadores_da_selecao = []
    id_selecao = trazer_id_por_nome(selecao, selecoes)
    for j in jogadores:
        if id_selecao == j['selecao_id']:
            jogadores_da_selecao.append(j)
    return jogadores_da_selecao

# Pedir atributos =============================================================
def obter_posisicao(prompt: str):
    posicoes_validas = ['Atacante', 'Goleiro', 'Meio', 'Zagueiro']

    while True:
        posicao = obter_texto(prompt).capitalize()
        if posicao in posicoes_validas:
            return posicao
        else:
            limpar_tela()
            print('\n\t| POSICAO INVALIDA. |\n\nVerifique se nao ha erros de ortografia ou se essa posicao e aceita pelo sistema.')


def obter_selecao(prompt: str, selecoes: list):
    while True:
        selecao = obter_texto(prompt).title()
        if trazer_id_por_nome(selecao, selecoes) != None:
            return selecao
        else:
            limpar_tela()
            print('\n| SELECAO NAO ENCONTRADA. |\n\nVerifique se nao ha erros de ortografia ou se essa selecao esta cadastrada no sistema.')

# Mensagem 