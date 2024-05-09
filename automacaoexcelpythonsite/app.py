#Ler dados da panilha 
#inserir cada celula de cada linha em um campo do sistema

#importando biblioteca de trabalho para usarmos nosso excel
import openpyxl
import mouse as ms
#importando biblioteca de automação de teclado e mouse
import pyautogui 

#importando o excel para dentro do programa e atribuindo a variavel workbook
workbook = openpyxl.load_workbook('automacaoexcelpythonsite/vendas_de_produtos.xlsx')
#Atribuindo apenas a pagina que iremos usar na nossa automação em uma nova varivael
vendas_sheet = workbook['vendas']

#para passar por todas  as linhas usaremos o metodo do openpyxl .iter_rows
for linha in vendas_sheet.iter_rows(min_row=2): #especificando que começa da linha 2
    #linha ira receber a linha como uma lista(list)
    # ["Murilo Barros","Cadeira	","434","Esportes"]
    #CLIENTE
    pyautogui.click(1334, 200, duration=1.5)
    pyautogui.write(linha[0].value)
    #PRODUTO
    pyautogui.click(1364, 230, duration=1.5)
    pyautogui.write(linha[1].value)
    #QUANTIDADE
    pyautogui.click(1346, 255, duration=1.5)
    pyautogui.write(str(linha[2].value))
    #CATEGORIA
    pyautogui.click(1423, 281, duration=1.5)
    pyautogui.write(linha[3].value)
    #SALVAR
    pyautogui.click(1278, 312, duration=1.5)
    #OK
    pyautogui.click(821, 568, duration=1.5)

