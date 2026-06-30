from persistencia import carregar_selecoes, salvar_selecoes, carregar_jogadores, salvar_jogadores, carregar_partidas, salvar_partidas
from Utils.utils_io import limpar_tela, obter_opcao, obter_texto, obter_inteiro_positivo, sucesso, obter_inteiro_faixa, obter_atributos, obter_grupo

from debbug import printar_elementos_in_list

from selecoes import cadastrar_selecao, ordenar_selecao_asc_desc, filtrar_por_atributo_ou_sigla, listar_selecoes, buscar_selecao_por_nome
from jogadores import cadastrar_jogador, obter_selecao, obter_posisicao, listar_jogadores, filtrar_jogadores, organizar_jogadores,  organizar_jogadores, listar_jogadores_filtrados, estatisticas#exibir_tabela_jogadores_bonita, exibir_tabela_jogadores_filtrados#, ordenar_jogadores_por_atributo, mostrar_jogadores_por_selecoes
from partidas import cadastrar_partida, listar_partidas, listar_tab_class_grupo

def main():
    limpar_tela()

    selecoes = carregar_selecoes()
    jogadores = carregar_jogadores()
    partidas = carregar_partidas()

    opcao = obter_opcao(exibir_menu_principal(len(selecoes), len(jogadores), len(partidas)), 0, 12)

    while opcao != 0:
        limpar_tela()
        if opcao == 1: # Opcao 1 ================================================================================
            print(f'\n\t---- CADASTRAR SELECAO ----\n')
            print(f'Digite as informacoes sobre a selecao que deseja cadastrar')
            nome = obter_texto(f'\nNOME: ').capitalize()
            confederacao = obter_texto(f'\nCONFEDERACAO: ').upper()
            grupo = obter_texto(f'\nGRUPO: ').upper()
            ranking_fifa = obter_inteiro_positivo(f'\nRANKING FIFA: ')
            titulos = obter_inteiro_positivo(f'\nNUMERO DE TITULOS: ')
            cadastrar_selecao(nome, confederacao, grupo, ranking_fifa, titulos, selecoes)
            sucesso()

        elif opcao == 2: #Opcao 2 ================================================================================
            print(f'\n\t---- LISTAR SELECOES ----\n')
            atributos_validos = ['nome', 'ranking_fifa', 'titulos']
            atributo = obter_atributos('\n\tOrdenar por qual atributo? (nome / ranking_fifa / titulos): ', atributos_validos)
            ordem = obter_inteiro_faixa('\n\tOrdem? (1 - Crescente / 2 - Decrescente): ', 1, 2)
            selecoes = ordenar_selecao_asc_desc(atributo, ordem, selecoes)
            listar_selecoes('Selecoes da Copa 2026', selecoes)
            sucesso()

        elif opcao == 3: #Opcao 3 ================================================================================
            print(f'\n\t---- BUSCAR SELECAO POR NOME ----\n')
            buscar_selecao_por_nome(selecoes)
        
        elif opcao == 4: #Opcao 4 ================================================================================
            atributos_validos = ['grupo', 'confederacao']
            continuar_buscando = 1
            while continuar_buscando != 0:
                print(f'\n\t---- FILTRAR SELECAO POR GRUPO OU CONFEDERACAO ----\n')
                atributo = obter_atributos(f'>> Deseja buscar por qual atributo? (grupo / confedercao): ', atributos_validos)
                valor_do_atributo = obter_texto(f'\nDIGITE O NOME DA CONFEDERACAO OU DO GRUPO: ').upper()
                selecoes_filtradas = filtrar_por_atributo_ou_sigla(valor_do_atributo, atributo, selecoes)
                mensagem_titulo = f'RESULTADOS ENCONTRADOS {atributo.upper()} COM: {valor_do_atributo}'
                listar_selecoes(mensagem_titulo, selecoes_filtradas)
                
                continuar_buscando = obter_opcao('\n\tDeseja fazer uma nova busca? \n\t1 - Sim | 0 - Nao : ', 0, 1)
            limpar_tela()

        elif opcao == 5: #Opcao 5 ================================================================================
            aviso = f'\t**AVISO: Para cadastrar um jogador e necessario que a selecao dele ja esteja cadastrada no sistema. \n\n\tDeseja continuar com o cadastro mesmo assim? (1 - Sim | 0 - Nao): '
            continuar_cadastrando = obter_opcao(aviso, 0, 1)
            limpar_tela()
            print(f'\n---- CADASTRAR JOGADOR ----\n')
            if continuar_cadastrando == 1:
                selecao = obter_selecao('Selecao: ', selecoes)
                nome_do_jogador = obter_texto(f'\nNome do jogador: ').title()
                posicao = obter_posisicao('\nPosicao (Goleiro/Zagueiro/Meio/Atacante): ')
                idade = obter_inteiro_faixa(f'\nIdade: ', 16, 55)
                gols = obter_inteiro_positivo(f'\nGols ate agora: ')

                cadastrar_jogador(selecao, posicao, nome_do_jogador, idade, gols, selecoes, jogadores)
                print(f"\n[OK] Jogador '{nome_do_jogador}' cadastrado e vinculado a selecao '{selecao}'")
                sucesso()

        elif opcao == 6: #Opcao 6 ================================================================================
            print(f'\n\t---- LISTAR JOGADORES ----\n')
            atributos_validos = ['nome', 'idade', 'gols']
            atributo = obter_atributos('\n\tOrdenar por qual atributo? (nome / idade / gols): ', atributos_validos)
            ordem = obter_inteiro_faixa('\n\tOrdem? (1 - Crescente / 2 - Decrescente): ', 1, 2)
            lista_jogadores_com_nome_selecao = organizar_jogadores(atributo, ordem, selecoes, jogadores)
            listar_jogadores('Jogadores Cadastrados', lista_jogadores_com_nome_selecao)
            sucesso()

        elif opcao == 7: #Opcao 7 ================================================================================
            atributos_validos = ['nome', 'idade', 'gols']
            continuar_buscando = 1
            while continuar_buscando != 0:
                print(f'\n\t---- FILTRAR JOGADORES ----\n')
                atributo = obter_atributos(f'>> Deseja buscar por qual atributo? (nome / idade / gols): ', atributos_validos)
                valor_do_atributo = obter_texto(f'\nDigite o nome, idade ou o numero de gols que deseja filtrar: ')
                jogadores_filtrados = filtrar_jogadores(atributo, valor_do_atributo, jogadores)
                mensagem_titulo = f'RESULTADOS ENCONTRADOS PARA {atributo.upper()} COM: {valor_do_atributo}'
                listar_jogadores_filtrados(mensagem_titulo, selecoes, jogadores_filtrados)

                continuar_buscando = obter_opcao('\n\tDeseja fazer uma nova busca? \n\t1 - Sim | 0 - Nao : ', 0, 1)
                limpar_tela()
            limpar_tela()

        elif opcao == 8: # Opcao 8 ================================================================================
            print(f'\n---- ARTILHEIROS E ESTATISTICAS ----\n')
            selecao = obter_selecao('Selecao: ', selecoes)
            estatisticas(selecao, selecoes, jogadores)

            sucesso()
        elif opcao == 9:  #Opcao 9 ================================================================================     
            aviso = f'\t**AVISO: Para cadastrar uma partida e necessario que as selecoes dela ja estejam cadastrada no sistema. \n\n\tDeseja continuar com o cadastro mesmo assim? (1 - Sim | 0 - Nao): '
            continuar_cadastrando = obter_opcao(aviso, 0, 1)
            limpar_tela()
            print(f'\n---- CADASTRAR PARTIDAS ----\n')
            atributos_validos = ['grupos','oitas_de_final', 'quartas_de_finais', 'semifinais', 'finais']
            if continuar_cadastrando == 1:
                selecao_da_casa = obter_selecao('Selecao da casa: ', selecoes).title()
                selecao_visitante = obter_selecao(f'\nSelecao visitante: ', selecoes).title()
                gols_da_selecao_de_casa = obter_inteiro_positivo('\nN de gols marcados pela selecao da casa: ')
                gols_da_selecao_visitante = obter_inteiro_positivo('\nN de gols marcados pela selecao visitante: ')
                fase = obter_atributos(f'\nFase: ', atributos_validos)

                cadastrar_partida(selecao_da_casa, selecao_visitante, gols_da_selecao_de_casa, gols_da_selecao_visitante, fase, selecoes, partidas)
                print(f"\n[OK] Partida cadastrada com sucesso.")
                sucesso()
        
        elif opcao == 10:  #Opcao 10 ================================================================================
            print(f'\n\t---- LISTAR PARTIDAS ----\n')
            listar_partidas(partidas, selecoes, 'PARTIDAS ENCONTRADAS')
            sucesso()

        elif opcao == 11:  #Opcao 11 ================================================================================
            aviso = f'\t**AVISO: Para ver a classificacao de um grupo ele estar cadastrado em uma selecao. \n\n\tDeseja continuar com a consulta mesmo assim? (1 - Sim | 0 - Nao): '
            
            continuar_buscando = obter_opcao(aviso, 0, 1)
            while continuar_buscando != 0:
                grupo = obter_grupo('\nQual grupo deseja consultar: ')
                limpar_tela()
                print(f'\n\t---- CLASSIFICACAO - GRUPO {grupo} ----\n')
                listar_tab_class_grupo(grupo, partidas, selecoes)
                continuar_buscando = obter_opcao('\n\tDeseja fazer uma nova consulta? \n\t1 - Sim | 0 - Nao : ', 0, 1)
            limpar_tela()
            
        elif opcao == 12:
            opcao_salvar = obter_opcao('\n>> Qual opcao deseja voce deseja salvar?\n\t1 - selecoes\n\t2 - jogadores\n\t3 - partidas\n\n\t> 0 - Sair\n>> ', 0, 3)
            while opcao_salvar != 0:
                if opcao_salvar == 1:
                    salvar_selecoes(selecoes)
                    print("Selecoes salvas com sucesso!")
                elif opcao == 2:
                    salvar_jogadores(jogadores)
                    print("\nJogadores salvos com sucesso!")
                elif opcao == 3:
                    salvar_partidas(partidas)
                    print("\nPartida salvas com sucesso!")
                opcao_salvar = obter_opcao('\n>> Qual opcao deseja voce deseja salvar?\n\t1 - selecoes\n\t2 - jogadores\n\t3 - partidas\n\n\t> 0 - Sair\n>> ', 0, 3)

        input('Pressione ENTER voltar ao menu...')
        limpar_tela()

        opcao = obter_opcao(exibir_menu_principal(len(selecoes), len(jogadores), len(partidas)), 0, 12)
    
    limpar_tela()
    print(f'Salvando dados...')
    salvar_selecoes(selecoes)
    print(f' - selecoes.txt ({len(selecoes)}) registros OK')
    salvar_jogadores(jogadores)
    print(f' - jogadores.txt ({len(jogadores)}) registros OK')
    salvar_partidas(partidas)
    print(f' - partidas.txt ({len(partidas)}) registros OK\n')


def exibir_menu_principal(qtd_selecoes: int, qtd_jogadores: int, qtd_partidas: int):
    menu = f'''
    ==============================================================
                    COPA MANAGER 2026 - FIFA 2026
    ==============================================================
    Status: {qtd_selecoes} selecoes | {qtd_jogadores} jogadores | {qtd_partidas} partidas
    --------------------------------------------------------------
    --------- SELECOES ---------
    1. Cadastrar selecao
    2. Listar / ordenar selecoes
    3. Buscar selecao por nome
    4. Filtrar por grupo ou confederacao

    --------- JOGADORES ---------
    5. Cadastrar jogador (vinculado a uma selecao)
    6. Listar / ordenar jogadores
    7. Filtrar jogadores
    8. Artilheiros e estatisticas (media de idade, total de gols)

    --------- PARTIDAS ---------
    9. Cadastrar Partida
    10. Listar Partidas
    11. Tabela de classificacao por grupo

    --------- SISTEMA ---------
    12. Salvar dados em arquivo
    0 - Sair (salva automaticamente)
    ===============================================================
    >>> Digite a opcao que deseja realizar: '''
    return menu

main()
