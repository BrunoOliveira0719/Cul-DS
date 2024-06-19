'''
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
'''
from datetime import datetime as dt, timedelta as td 
from clear import clear

livros_retirados = []

armazenamento_de_usuarios = ['admin']
armazenamento_de_senhas = ['12345']

def menu():
  print('Bem vindo ao sistema de gerenciamento de livros da biblioteca\n ')
  print('O que deseja fazer?\n ')
  print('1 - Para pegar um livro')
  print('2 - Para fazer login do adm')
  print('3 - Para devolver um livro')
  print('4 - Para sair')

  opcao = int(input('Digite a opção desejada: '))

  if opcao == 1:
    clear()
    retirar_livro()
  elif opcao == 2:
    clear()
    login_adm()
  elif opcao == 3:
    clear()
    devolver_livro()
  elif opcao == 4:
    print('Saindo do sistema...')
    exit()

def retirar_livro():
  print('Para retirar um livro, digite as seguintes informções:\n ')
  
  nome_aluno = input('Digite seu nome: ')
  RA = input('Digite o seu RA: ')
  livro = input('Digite o livro que deseja retirar: ')
  categoria = input('Digite a categoria do livro: ')
  responsavel = input('Digite o nome do responsável: ')
  data_retirada = dt.now().date()
  data_entrega = data_retirada + td(days=20)

  print(f'Você retirou o livro {livro} no dia {data_retirada} com sucesso!\nVocê aluno com RA {RA} deve entregar o livro até {data_entrega}!')

  print('Até a proxima!')

  livros_retirados.append({
      'Nome do aluno': nome_aluno,
      'RA': RA,
      'livro': livro,
      'categoria': categoria,
      'responsavel': responsavel,
      'data retirada': data_retirada,
      'data entrega': data_entrega
  })

def devolver_livro():
  print('Para devolver um livro, digite as seguintes informções:\n ')
  
  RA = input('Digite o seu RA: ')
  livro = input('Digite o livro que deseja devolver: ')
  data_devolucao = dt.now().date()

  for livro_a_devolver in livros_retirados:
    if livro == livro_a_devolver['livro'] and RA == livro_a_devolver['RA']:
      livros_retirados.remove(livro_a_devolver)
      print(f'Você devolveu o livro {livro} no dia {data_devolucao} com sucesso!')
    else:
      print('Livro ou RA incorreto!')

  print('Até a proxima!')

def mostrar_livros_retirados():
  for livro in livros_retirados:
      print(f"O livro '{livro['livro']}' foi retirado por {livro['RA']} na data {livro['data_retirada']} e deve ser devolvido até {livro['data_entrega']}.")

def login_adm():
  print('Para fazer login do adm, digite as seguintes informções:\n ')
  
  login = input('Digite o Usuario: ')
  senha = input('Digite a senha: ')
  for login in armazenamento_de_usuarios:
    if login == login:
      for senha in armazenamento_de_senhas:
        if senha == senha: 
          print('Login efetuado com sucesso')
          print('Você quer ver os livros retirados?\nDigite S para sim e N para não')
          resposta = input('Resposta: S/N ').upper()
          if resposta == 'S':
            mostrar_livros_retirados()
          else:
            print('Ok, obrigado por usar nosso sistema')
          
        else:
         print('Senha incorreto ou tu não é ADM')

    else:
      print('Login incorreto ou tu não é ADM')

menu()
