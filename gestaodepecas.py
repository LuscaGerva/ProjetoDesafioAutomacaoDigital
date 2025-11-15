def menudeopcoes():
    print("\nMenu de opções:")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas")
    print("3. Listar peças reprovadas")
    print("4. Remover peça cadastrada aprovada")
    print("5. Listar caixas fechadas")
    print("6. Gerar relatório final")
    print("0. Sair do projeto")


limite_caixa = 10
caixas_pecas_aprovadas = []
caixa_pecas_reprovada = []
opcao = ""

print("Bem-vindo!\n")
while opcao != "0":
    menudeopcoes()
    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        print("================= Cadastro de Peças =================")
        id_peca = input("Insira o id da peça: ")
        peso_peca = float(input("Insira o peso da peça em gramas (apenas número): "))
        comprimento_peca = float(input("Insira o comprimento da peça (em centímetros): "))
        cor_peca = input("Insira a cor da peça (tudo mínusculo): ")

        if (peso_peca >= 95 and peso_peca <= 105) and (cor_peca.lower() in ["azul", "verde"]) and (10 <= comprimento_peca <= 20):
            print(f"\nPeça {id_peca} APROVADA\n")
            pecaaprovada = {
                "id": id_peca,
                "peso": peso_peca,
                "cor": cor_peca,
                "comprimento": comprimento_peca
            }
            if not caixas_pecas_aprovadas or len(caixas_pecas_aprovadas[-1]) >= limite_caixa:
                caixas_pecas_aprovadas.append([])
                print(f"Nova caixa criada. Total de caixas: {len(caixas_pecas_aprovadas)}")
            
            caixas_pecas_aprovadas[-1].append(pecaaprovada)
            print(f"Peça adicionada na caixa {len(caixas_pecas_aprovadas)}. Itens na caixa: {len(caixas_pecas_aprovadas[-1])}/{limite_caixa}")
        else:
            print(f"\nPeça {id_peca} REPROVADA\n")
            caixa_pecas_reprovada.append({
                "id": id_peca,
                "peso": peso_peca,
                "cor": cor_peca,
                "comprimento": comprimento_peca
            })
    
    elif opcao == "2":
        print("================= Peças Aprovadas =================")
        if caixas_pecas_aprovadas:
            for i, caixa in enumerate(caixas_pecas_aprovadas, 1):
                status = "FECHADA" if len(caixa) == limite_caixa else f"ABERTA ({len(caixa)}/{limite_caixa})"
                print(f"\nCaixa {i} - Status: {status}")
                for peca in caixa:
                    print(f"  ID: {peca['id']}, Peso: {peca['peso']}g, Cor: {peca['cor']}, Comprimento: {peca['comprimento']}cm")
        else:
            print("Nenhuma peça aprovada encontrada.")

    elif opcao == "3":
        print("================= Peças Reprovadas =================")
        if caixa_pecas_reprovada:
            for peca in caixa_pecas_reprovada:
                print(f"ID: {peca['id']}, Peso: {peca['peso']}g, Cor: {peca['cor']}, Comprimento: {peca['comprimento']}cm")
        else:
            print("Nenhuma peça reprovada encontrada.")

    elif opcao == "4":
        print("================= Remover Peça Aprovada =================")
        id_remover = input("Digite o ID da peça que deseja remover: ")
        removida = False
        for caixa in caixas_pecas_aprovadas:
            peca_para_remover = None
            for peca in caixa:
                if peca["id"] == id_remover:
                    peca_para_remover = peca
                    break 
            
            if peca_para_remover:
                caixa.remove(peca_para_remover)
                print(f"Peça {id_remover} removida com sucesso.")
                removida = True
                break
            
        if not removida:
            print("Peça não encontrada.")

    elif opcao == "5":
        print("================= Caixas Fechadas =================")
        caixas_fechadas_encontradas = False
        for i, caixa in enumerate(caixas_pecas_aprovadas, 1):
            if len(caixa) == limite_caixa:
                print(f"Caixa {i} está FECHADA (contém {len(caixa)} peças).")
                caixas_fechadas_encontradas = True
        
        if not caixas_fechadas_encontradas:
            print("Nenhuma caixa fechada encontrada.")

    elif opcao == "6":
        print("================= Relatório Final =================")
        total_aprovadas = sum(len(caixa) for caixa in caixas_pecas_aprovadas)
        total_reprovadas = len(caixa_pecas_reprovada)
        total_pecas = total_aprovadas + total_reprovadas
        
        print(f"Total de peças cadastradas: {total_pecas}")
        print(f"Total de peças aprovadas: {total_aprovadas}")
        print(f"Total de peças reprovadas: {total_reprovadas}")
        print(f"Total de caixas utilizadas: {len(caixas_pecas_aprovadas)}")

    elif opcao == "0":
        print("Saindo do projeto...")
        break

    else:
        print("Opção inválida! Tente novamente.")