from rich.console import Console
from rich.table import Table

from Utils.utils import filtrar_por_atributo_ou_sigla, ordenar_lista_asc_desc
from Utils.utils_io import limpar_tela, obter_texto, obter_opcao

console = Console()

# Cadastrar Selecoes (Opcao 1) ====================================================================================
def cadastrar_selecao(nome: str, confederacao: str, grupo: str, ranking_fifa: int, titulos: int, selecoes: list):
    id = criar_id(selecoes)
    nova_selecao = {
        'id': id,
        'nome': nome,
        'confederacao': confederacao,
        'grupo': grupo,
        'ranking_fifa': ranking_fifa,
        'titulos': titulos
        }
    selecoes.append(nova_selecao)
    return selecoes

def criar_id(selecoes: list):
    id = len(selecoes)
    ids_existentes = []
    for s in selecoes:
        ids_existentes.append(s['id'])
    if id in ids_existentes:
        id += 1 
    

# Mostrar Selecoes (Opcao 2) ====================================================================================
def listar_selecoes(titulo_da_tabela: str, registros: str):
    exibir_tabela_selecoes(titulo_da_tabela, registros)

def ordenar_selecao_asc_desc(atributo: str, ordem: int, selecoes:list):
    selecoes_ordenadas = ordenar_lista_asc_desc(atributo, selecoes, ordem)
    return selecoes_ordenadas

# Buscar selecoes por nome (Opcao 3) ===============================================================================
def buscar_selecao_por_nome(selecoes: list):
    continuar_buscando = 1
    while continuar_buscando != 0:       
        nome_ditado = obter_texto(f'>> Digite o nome da selecao que deseja buscar: ')
        selecoes_filtradas = filtrar_selecao_por_nome(nome_ditado, 'nome', selecoes)
        mensagem_titulo = f'RESULTADOS ENCONTRADOS COM: {nome_ditado}'

        if selecoes_filtradas == None or selecoes_filtradas == []:
            print(f'\n\t{mensagem_titulo}\n\tAte o momento ainda nao ha selecoes cadastradas com este nome ou sigla.')
        else:
            listar_selecoes(mensagem_titulo, selecoes_filtradas)
            
        continuar_buscando = obter_opcao('\n\tDeseja fazer uma nova busca? \n\t1 - Sim | 0 - Nao : ', 0, 1)
        limpar_tela()

def filtrar_selecao_por_nome(parte_do_nome: str, atributo, selecoes: list):
    selecoes_filtradas = filtrar_por_atributo_ou_sigla(parte_do_nome, atributo, selecoes)
    return selecoes_filtradas

# Funcoes para exibir tabelas ===============================================================================
def exibir_tabela_selecoes_grupo(titulo_da_tabela: str, selecoes: list):
    if selecoes == None or selecoes == []:
        print(f'\n\t{titulo_da_tabela}\n\tAte o momento ainda nao ha selecoes cadastradas com este grupo ou confederacao.')
    else:
        limpar_tela()

        tabela = Table(title=titulo_da_tabela)
        tabela.add_column("ID", justify="right", style="cyan")
        tabela.add_column("Selecao", style="bold")
        tabela.add_column("Confederacao", justify="center")
        tabela.add_column("Grupo", justify="center")
        tabela.add_column("Ranking FIFA", justify="right", style="green")
        tabela.add_column("Titulos", justify="right", style="green")

        for selecao in selecoes:
            tabela.add_row(str(selecao["id"]), selecao["nome"], selecao["confederacao"], selecao["grupo"], str(selecao["ranking_fifa"]), str(selecao["titulos"]))
        console.print(tabela)

def exibir_tabela_selecoes(titulo_da_tabela: str, selecoes: list):
    if selecoes == None or selecoes == []:
        print(f'\n\t{titulo_da_tabela}\n\tAte o momento ainda nao ha selecoes cadastradas.')
    else:
        limpar_tela()

        tabela = Table(title=titulo_da_tabela)
        tabela.add_column("ID", justify="right", style="cyan")
        tabela.add_column("Selecao", style="bold")
        tabela.add_column("Confederacao", justify="center")
        tabela.add_column("Grupo", justify="center")
        tabela.add_column("Ranking FIFA", justify="right", style="green")
        tabela.add_column("Titulos", justify="right", style="green")

        for selecao in selecoes:
            tabela.add_row(str(selecao["id"]), selecao["nome"], selecao["confederacao"], selecao["grupo"], str(selecao["ranking_fifa"]), str(selecao["titulos"]))
        console.print(tabela)

