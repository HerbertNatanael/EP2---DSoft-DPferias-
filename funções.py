def transforma_base(questoes):
    base = {}

    for questao in questoes:
        nivel = questao["nivel"]

        if nivel not in base:
            base[nivel] = []

        base[nivel].append(questao)

    return base

def valida_questao(questao):
    retorno = {}

    if "titulo" not in questao:
        retorno["titulo"] = "nao_encontrado"

    if "nivel" not in questao:
        retorno["nivel"] = "nao_encontrado"

    if "opcoes" not in questao:
        retorno["opcoes"] = "nao_encontrado"

    if "correta" not in questao:
        retorno["correta"] = "nao_encontrado"

    if len(questao) != 4:
        retorno["outro"] = "numero_chaves_invalido"

    if "titulo" in questao:
        if isinstance(questao["titulo"], str) and questao["titulo"].strip() == "":
            retorno["titulo"] = "vazio"

    if "nivel" in questao:
        if questao["nivel"] not in ["facil", "medio", "dificil"]:
            retorno["nivel"] = "valor_errado"

    if "opcoes" in questao:
        opcoes = questao["opcoes"]

        if len(opcoes) != 4:
            retorno["opcoes"] = "tamanho_invalido"
        else:
            chaves_validas = ["A", "B", "C", "D"]

            if list(opcoes.keys()) != chaves_validas:
                retorno["opcoes"] = "chave_invalida_ou_nao_encontrada"
            else:
                vazias = {}

                for chave in chaves_validas:
                    if isinstance(opcoes[chave], str) and opcoes[chave].strip() == "":
                        vazias[chave] = "vazia"

                if vazias != {}:
                    retorno["opcoes"] = vazias


    if "correta" in questao:
        if questao["correta"] not in ["A", "B", "C", "D"]:
            retorno["correta"] = "valor_errado"

    return retorno

def valida_questoes(questoes):
    retorno = []

    for questao in questoes:
        retorno.append(valida_questao(questao))

    return retorno