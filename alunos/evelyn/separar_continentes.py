"""
Separa continentes em tabelas separadas.
"""

import sys
import pandas as pd

# carrega o DataFrame
df = pd.read_csv(sys.argv[1], index_col='country')

# cria lista com continentes
continents = list(df['continent'].unique())

# roda for loop na lista
for item in continents:
    df_item = df[df['continent'] == item]
    file_name = 'gapminder_' + item + '.csv'
    df_item.to_csv(file_name)
    print("DataFrame com continente", item, "foi escrito em", file_name)
    
    
breakpoint()
    
print("Feito!")
