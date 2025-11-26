import pandas as pd
import os

"""
Concatenate all CSV files in the script folder ending with '_final.csv',
clean the 'forma_pag' column by replacing 'NAN' with 'NÃO CHECADO' and
'PIX DIRETO' with 'PIX', then save the combined dataframe as 'total_sales.csv'.
"""

pasta = os.path.dirname(os.path.abspath(__file__))      
pasta_raiz = os.path.dirname(pasta)                     
saida = os.path.join(pasta_raiz, 'Sales_Data')     



arquivos = [f for f in os.listdir(pasta) if f.endswith('_final.csv')]
df_final = pd.concat([pd.read_csv(os.path.join(pasta, f), on_bad_lines='skip') for f in arquivos], ignore_index=True)
df_final['forma_pag'] = df_final['forma_pag'].replace({
    "NAN": "NÃO CHECADO",
    "PIX DIRETO": "PIX"
})
df_final.to_csv(os.path.join(saida, "total_vendas.csv"), index=False, encoding="utf-8-sig")
