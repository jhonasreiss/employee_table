import os
import pandas as pd
import random

try:
    if os.path.exists('sheets'):
        print('existe!')
    else:
        os.makedirs('data_sheet')
except:
    print('Pasta já existe!')

nome = []
with open('content_base/names.txt','r',encoding='utf-8') as file:
    for i in file:
        nome.append(i)

salario = [random.randint(1200,5600) for i in range(nome.__len__())]
idade = [random.randint(17,35) for i in range(nome.__len__())]
imposto = 9
redução_imposto = []
salario_final = []

for i in range(salario.__len__()):
    redução_imposto.append((salario[i] * imposto)/100)
    salario_final.append(salario[i] - redução_imposto[i])

dados_ficticios = {'Nome':nome,'Salário Líquido':salario,'Idade':idade,'Imposto':redução_imposto,'Salário Real':salario_final}

planilha = pd.DataFrame(dados_ficticios)
planilha.to_excel('content_base/Lista de Funcionários.xlsx',index=False)
print(planilha)