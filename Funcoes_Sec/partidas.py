from rich.console import Console
from rich.table import Table

from Utils.utils import trazer_id_por_nome, trazer_nome_selecao_por_id, filtrar_por_valor_do_atributo, ordenar_lista_asc_desc
from Utils.utils_io import limpar_tela

console = Console()

# Opcao 9 =======================================================================
def cadastrar_partida(selecao_da_casa: str, selecao_visitante: str,  gols_da_selecao_de_casa: int, gols_da_selecao_visitante: int, fase: str, selecoes: list, partidas: list):
    id_partida = criar_id_partida(partidas)
    id_selecao_casa = trazer_id_por_nome(selecao_da_casa, selecoes)
    id_selecao_visitante = trazer_id_por_nome(selecao_visitante, selecoes)
    nova_partida = {'id': id_partida, 
                    'selecao_casa_id': id_selecao_casa, 
                    'selecao_fora_id': id_selecao_visitante, 
                    'gols_casa': gols_da_selecao_de_casa, 
                    'gols_fora': gols_da_selecao_visitante, 
                    'fase': fase}
    partidas.append(nova_partida)
    return partidas

def criar_id_partida(partidas: list):
    id_partida = 500 + len(partidas)
    return id_partida

# Opcao 10 =======================================================================
def listar_partidas(partidas: list, selecoes: list, titulo_tabela: str):
    lista_partidas_str = montar_lista_partidas(partidas, selecoes)
    exibir_tabela_partidas(titulo_tabela, lista_partidas_str)

def montar_lista_partidas(partidas: list, selecoes: list):
    lista_partidas_str = []
    for p in partidas:
        selecao_da_casa = trazer_nome_selecao_por_id(selecoes, p, 'selecao_casa_id')
        selecao_visitante = trazer_nome_selecao_por_id(selecoes, p, 'selecao_fora_id')
        fase = p['fase']
        if '_' in fase:
            fase.replace('_', ' ')
        partida = f'{selecao_da_casa} {p['gols_casa']} x {p['gols_fora']} {selecao_visitante} ({fase.title()})'
        lista_partidas_str.append(partida)
    return lista_partidas_str

def exibir_tabela_partidas(titulo_tabela: str, lista_de_partidas: list):
        limpar_tela()
        if lista_de_partidas == None or lista_de_partidas == []:
            limpar_tela()
            print(f'\n\t{titulo_tabela}\n\tAte o momento ainda nao ha partidas cadastradas.')
        else:
            limpar_tela()
            tabela = Table(title=titulo_tabela)
            tabela.add_column("Partidas", style="bold", justify="center")

            for i in lista_de_partidas:
                tabela.add_row(i)
            console.print(tabela)

# Opcao 11 =======================================================================
def listar_tab_class_grupo(grupo: str, partidas: list, selecoes: list):
    selecoes_no_grupo = filtrar_selecoes_grupo(grupo, selecoes)
    estatisticas = formar_estisticas_selecoes(selecoes_no_grupo, partidas)
    exibir_tabela_estatisticas(estatisticas)

def filtrar_selecoes_grupo(grupo: str, selecoes: list):
    selecoes_no_grupo = filtrar_por_valor_do_atributo('grupo', grupo, selecoes)
    return selecoes_no_grupo

def formar_estisticas_selecoes(lista_selecoes: list, partidas: list):
    estatisticas = []
    for s in lista_selecoes:
        nova_estatistica = calcular_estatisticas_selecoes(s, partidas)
        estatisticas.append(nova_estatistica)
    estatisticas_ordenadas = ordenar_estatisticas(estatisticas)
    return estatisticas_ordenadas

def ordenar_estatisticas(estatisticas):
    estatisticas_ordenadas = []
    estatisticas = ordenar_lista_asc_desc('pontos', estatisticas, ordem=2)
    i = 1
    for e in estatisticas:
        nova_estatistica = {'posicao': i, 
                            'selecao': e['selecao'], 
                            'pontos': e['pontos'], 
                            'vitorias': e['vitorias'], 
                            'empates': e['empates'], 
                            'derrotas': e['derrotas'], 
                            'gols_pro': e['gols_pro'], 
                            'gols_contra': e['gols_contra'], 
                            'saldo_gols': e['saldo_gols']}
        estatisticas_ordenadas.append(nova_estatistica)
        i += 1

    return estatisticas_ordenadas

def calcular_estatisticas_selecoes(selecao: dict, partidas: list):
    partidas_da_selecao = filtrar_partidas(selecao, partidas)
    nome_selecao = selecao['nome']
    vitorias = calcular_vitorias(selecao, partidas_da_selecao)
    empates = calcular_empates(selecao, partidas_da_selecao)
    derrotas = calcular_derrotas(selecao, partidas_da_selecao)
    gols_pro = calcular_gols_pro(selecao, partidas_da_selecao)
    gols_contra = calcular_gols_contra(selecao, partidas_da_selecao)
    saldo_gols = gols_pro - gols_contra
    pontos = gols_pro + saldo_gols
    estatistica = {'selecao': nome_selecao, 'pontos': pontos, 'vitorias': vitorias, 'empates': empates, 'derrotas': derrotas, 'gols_pro': gols_pro, 'gols_contra': gols_contra, 'saldo_gols': saldo_gols}
    return estatistica


def calcular_gols_pro(selecao: dict, partidas: list):
    somatorio_gols_pro = 0
    for p in partidas:
        if selecao['id'] == p['selecao_casa_id']:
            somatorio_gols_pro += p['gols_casa']
        elif selecao['id'] == p['selecao_fora_id']:
            somatorio_gols_pro += p['gols_fora']
    return somatorio_gols_pro

def calcular_gols_contra(selecao: dict, partidas: list):
    somatorio_gols_contra = 0
    for p in partidas:
        if selecao['id'] == p['selecao_casa_id']:
            somatorio_gols_contra += p['gols_fora']
        elif selecao['id'] == p['selecao_fora_id']:
            somatorio_gols_contra += p['gols_casa']
    return somatorio_gols_contra

def calcular_vitorias(selecao: dict, partidas: list):
    vitorias = 0
    for p in partidas:
        if selecao['id'] == p['selecao_casa_id']:
            if p['gols_casa'] > p['gols_fora']:
                vitorias += 1
        elif selecao['id'] == p['selecao_fora_id']:
            if p['gols_fora'] > p['gols_casa']:
                vitorias += 1
    return vitorias

def calcular_empates(selecao: dict, partidas: list):
    empates = 0
    for p in partidas:
        if selecao['id'] == p['selecao_casa_id']:
            if p['gols_casa'] == p['gols_fora']:
                empates += 1
        elif selecao['id'] == p['selecao_fora_id']:
            if p['gols_fora'] == p['gols_casa']:
                empates += 1
    return empates

def calcular_derrotas(selecao: dict, partidas: list):
    derrotas = 0
    for p in partidas:
        if selecao['id'] == p['selecao_casa_id']:
            if p['gols_casa'] == p['gols_fora']:
                derrotas += 1
        elif selecao['id'] == p['selecao_fora_id']:
            if p['gols_fora'] == p['gols_casa']:
                derrotas += 1
    return derrotas

def filtrar_partidas(selecao: dict, partidas: list):
    partidas_filtradas = []
    for p in partidas:
        if selecao['id'] == p['selecao_casa_id'] or selecao['id'] == p['selecao_fora_id']:
            partidas_filtradas.append(p)
    return partidas_filtradas

def exibir_tabela_estatisticas(estatisticas: list):
    if estatisticas == None or estatisticas == []:
        limpar_tela()
        print(f'\n\tNENHUMA SELECAO ENCONTRADA\n\tAte o momento ainda nao ha selecoes cadastradas neste grupo.')
    else:
        limpar_tela()
        tabela = Table(title='')
        tabela.add_column("Pos", justify="right", style="cyan")
        tabela.add_column("Selecao", style="bold")
        tabela.add_column("P", justify="center")
        tabela.add_column("V", justify="center")
        tabela.add_column("E", justify="center")
        tabela.add_column("D", justify="center")
        tabela.add_column("GP", justify="center", style="green")
        tabela.add_column("GC", justify="center", style="red")
        tabela.add_column("SG", justify="center")

        for e in estatisticas:
            tabela.add_row(str(e["posicao"]), e["selecao"], str(e["pontos"]), str(e["vitorias"]), str(e["empates"]), str(e["derrotas"]), str(e["gols_pro"]), str(e["gols_contra"]), str(e["saldo_gols"]))
        console.print(tabela)

        


