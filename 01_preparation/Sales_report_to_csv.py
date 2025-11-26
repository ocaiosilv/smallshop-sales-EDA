import pandas as pd
import os

"""
What i need to change between the different reports was only this and the ARQUIVO name:

(1) LINE 34 → DATE index on the "Nº NFC-e:" line
(2) LINE 41 → DATE index on the "Nº nota:" line
(3) LINE 43 → PAYMENT METHOD index (previous value)
(4) LINE 52 → CLIENT index
(5) LINE 62 → PRODUCT DESCRIPTION index
(6) LINE 63 → PRODUCT UNIT PRICE index
(7) LINE 64 → PRODUCT QUANTITY index
----------------------------------------------------------------
"""

nome_arquivo = "ReportSalesPt1"
script_dir = os.path.dirname(os.path.abspath(__file__))
pasta = os.path.join(script_dir, "SReports")
caminho = os.path.join(pasta, nome_arquivo)

df = pd.read_excel(caminho, header=None)

abc = {
    "data": [],
    "cliente": [],
    "id_produto": [],
    "descricao": [],
    "quantidade": [],
    "valor_und": [],
    "forma_pag": [],
}

blocks = {}
lista_produtos_vistos = {}
turn = 0
a = -1

for i in range(len(df)):

    if df.iloc[i, 0] == "Nº NFC-e:":
        turn = 0
        a += 1
        if a not in blocks:
            blocks[a] = []
        blocks[a].append(df.iloc[i, 20])  ## get date
        continue

    elif df.iloc[i, 0] == "Nº nota:":
        turn = 1
        a += 1
        if a not in blocks:
            blocks[a] = []
        blocks[a].append(df.iloc[i, 20])  ## get date
        previous_value = df.iloc[i-1, 0]  # get previous value from column 0
        if not pd.isna(previous_value):    # check if it's not NaN
            blocks[a].append(previous_value)
        else:
            blocks[a].append("not checked")  # if NaN, add markers
        continue

    if df.iloc[i, 0] == "Cliente:":
        blocks[a].append(df.iloc[i, 4])  ## get client

    try:
        prod_code = int(df.iloc[i, 0])  # check if it's a product code
        blocks[a].append(prod_code)     # append product code
        lista_produtos_vistos[prod_code] = [
            df.iloc[i, 2],              ## product description
            df.iloc[i, 11]              ## unit price
        ]
        blocks[a].append(df.iloc[i, 10])  ## quantity
    except:
        pass

for i in range(len(blocks)):
    data = blocks[i][0]
    forma_pag = blocks[i][1]
    cliente = blocks[i][2]

    for w in range(3, len(blocks[i]), 2):
        abc["data"].append(data)
        abc["cliente"].append(cliente)
        abc["id_produto"].append(blocks[i][w])
        abc["descricao"].append(lista_produtos_vistos[blocks[i][w]][0])
        abc["quantidade"].append(blocks[i][w+1])
        abc["valor_und"].append(lista_produtos_vistos[blocks[i][w]][1])
        abc["forma_pag"].append(forma_pag)

saida = os.path.join(pasta, nome_arquivo.replace(".xls", "_final.csv"))
pd.DataFrame(abc).to_csv(saida, index=False, encoding="utf-8-sig")
