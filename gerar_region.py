import os

def gerar_codigo_tableau(caminho_txt):
    with open(caminho_txt, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    codigo = "IF "
    primeira = True
    continente_atual = ""
    buffer_paises = []

    for linha in linhas:
        linha = linha.strip()

        if linha.endswith(":"):
            if continente_atual and buffer_paises:
                condicao = '[Country or region] IN (' + ', '.join(f'"{p}"' for p in buffer_paises) + ')'
                if primeira:
                    codigo += f"{condicao} THEN \"{continente_atual}\"\n"
                    primeira = False
                else:
                    codigo += f"ELSEIF {condicao} THEN \"{continente_atual}\"\n"
                buffer_paises = []

            continente_atual = linha[:-1]
        elif linha:
            buffer_paises += [p.strip() for p in linha.split(",") if p.strip()]

    if continente_atual and buffer_paises:
        condicao = '[Country or region] IN (' + ', '.join(f'"{p}"' for p in buffer_paises) + ')'
        if primeira:
            codigo += f"{condicao} THEN \"{continente_atual}\"\n"
        else:
            codigo += f"ELSEIF {condicao} THEN \"{continente_atual}\"\n"

    codigo += 'ELSE "Other"\nEND'

    with open("codigo_tableau_gerado.txt", "w", encoding='utf-8') as out:
        out.write(codigo)

    print("✅ Código Tableau gerado com sucesso em 'codigo_tableau_gerado.txt'")

gerar_codigo_tableau("paises_por_continente.txt")