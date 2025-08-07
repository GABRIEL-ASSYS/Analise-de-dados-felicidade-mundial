import pandas as pd

arquivos = {
    '2015': '2015.csv',
    '2016': '2016.csv',
    '2017': '2017.csv',
    '2018': '2018.csv',
    '2019': '2019.csv'
}

dfs = []

for ano, nome_arquivo in arquivos.items():
    df = pd.read_csv(nome_arquivo, encoding='utf-8', sep=',')
    df['Ano'] = int(ano)
    dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)

df_final.to_csv('dados_combinados.xlsx', index=False)

print("✅ Arquivos combinados com sucesso! Arquivo salvo como 'dados_combinados.csv'")