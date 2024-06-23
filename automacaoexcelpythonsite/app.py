#Ler dados da panilha 
#inserir cada celula de cada linha em um campo do sistema

#importando biblioteca de trabalho para usarmos nosso excel
import openpyxl
import mouse as ms
#importando biblioteca de automação de teclado e mouse

import defs
#importando o excel para dentro do programa e atribuindo a variavel workbook
workbook = openpyxl.load_workbook('automacaoexcelpythonsite/vendas_de_produtos.xlsx')
#Atribuindo apenas a pagina que iremos usar na nossa automação em uma nova varivael
vendas_sheet = workbook['vendas']

#para passar por todas  as linhas usaremos o metodo do openpyxl .iter_rows
defs.BuscaLinhas(vendas_sheet)

