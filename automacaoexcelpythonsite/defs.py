import pyautogui 

def BuscaLinhas(vendas_sheet):
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