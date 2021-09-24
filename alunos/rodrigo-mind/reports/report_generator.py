import sys
import pandas as pd
from jinja2 import Environment, FileSystemLoader


def main(customers_file, template):
    # Carregar os dados
    df = pd.read_excel(customers_file)
    print("Carregando", len(df), "clientes.")
    
    # Formatacao
    df['primeiro_nome'] = df["Cliente"].str.split(expand=True).iloc[:, 0]
    df.rename(columns={"Cliente": "cliente",
                       "Mês": "mes",
                       "12m": "doze_meses"}, inplace=True)
    
    # Carregar template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template)
    
    # Iterar linhas do DataFrame
    for ix, row in df.iterrows():   # ix: nome da linha, row: objeto pd.Series
        
        # Formatando o nome do cliente para usar no nome do relatorio
        cliente_formatado = row["cliente"].lower().replace(" ", "_")
        
        # Dicionario de variaveis a serem inseridas no template
        template_vars = row.to_dict()
        
        # String com corpo HTML do relatorio
        html_out = template.render(template_vars)
        
        outfile = f"report_{cliente_formatado}.html"
        print("Gerando relatório em:", outfile)
        
        # Abrindo o arquivo com nome do cliente e escrevendo o HTML
        with open(outfile, "w") as f:
            f.write(html_out)
            

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
