import openpyxl as xl
from datetime import datetime as dt, timedelta as td 


RA = input('digite o seu RA: ')
livro = input('digite o livro que deseja retirar: ')
categoria = input('digite a categoria do livro: ')
responsavel = input('digite o nome do responsavel: ')


data_retirada = dt.now().date()
data_entrega = data_retirada + td(days= 20)

print(data_retirada)
print(data_entrega)
