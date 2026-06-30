def trazer_nome_selecao_por_id(selecoes: list, dicionario: dict, atributo_id: str):
    for selecao in selecoes:
        if dicionario[atributo_id] == selecao['id']:
            nome = selecao['nome']
            return nome

def trazer_id_por_nome(atributo_nome: str, lista_de_registro: list):
    for registro in lista_de_registro:
        if atributo_nome == registro['nome']:
            id_resgistro = registro['id']
            return id_resgistro 
    return None

def filtrar_por_atributo_ou_sigla(parte_do_nome_do_atributo: str, atributo:str, registros: list):
    itens_filtrados = []
    for item in registros:
        if (parte_do_nome_do_atributo.capitalize() in str(item[atributo])) or (parte_do_nome_do_atributo in str(item[atributo])):
            itens_filtrados.append(item)
    return itens_filtrados

def filtrar_por_valor_do_atributo(atributo: str, valor_atributo: str, lista: list):
    itens_filtrados = []
    for item in lista:
        if item[atributo] == valor_atributo:
            itens_filtrados.append(item)
    return itens_filtrados

def ordenar_lista_asc_desc(atributo: str, lista:list, ordem: int):
    if ordem == 1:
        lista = sorted(lista, key=lambda item: item[atributo])
        return lista
    elif ordem == 2:
        lista = sorted(lista, key=lambda item: item[atributo], reverse=True)
        return lista
    
def formar_str_separada_por_virgula(lista: list):
    jogadores = []
    for j in lista:
        jogadores.append(j['nome'])

    separador = ','
    conjunto_de_palavras = separador.join(jogadores)
    return conjunto_de_palavras
        