import json
from datetime import datetime

def tranferencia_contas():
  print()
  print('Você está em Tranferencia entre Bancos!')
  print()
  
  cpf = input("Digite o CPF de origem: ")
  senha = input("Digite a senha de origem: ")
  cpf_destino = input("Digite o de CPF destino: ")
  valor = float(input("Digite o valor que deseja transferir: "))

  
  with open ("arquivo.json", "r") as f:
    clientes = json.load(f)

  
  for cliente in clientes:
    if cliente["cpf"] == cpf and cliente["senha"] == senha:
      cliente["valor_inicio"] -= valor
    if cliente["cpf"] == cpf_destino:
      cliente["valor_inicio"] += valor

      
  with open("arquivo.json", "w") as f:
    json.dump(clientes, f)

  print(clientes)
  
def cliente_novo():
  print()
  print('Você está em Novo Cliente!')
  print()


  cliente_new = dict()
  cliente_new['nome'] = input("Digite seu nome: ")
  cliente_new['cpf'] = int(input("Digite seu CPF: "))
  cliente_new['tipo_conta'] = input("Digite o tipo da sua conta: ")
  cliente_new['valor_conta'] =  int(input("Digite o valor inicial da conta: "))
  cliente_new['senha'] = input("Digite sua senha: ")


  with open('arquivo.json', 'r') as Novo_Cliente:
    Cliente_New = json.load(Novo_Cliente)

  Cliente_New.append(cliente_new)
    
  with open('arquivo.json', 'w') as Novo_Cliente:
    json.dump(Cliente_New, Novo_Cliente)

  data = datetime.now()
  extrato = dict()
  extrato['cpf'] = cliente_new['cpf']
  extrato['valor'] = cliente_new['valor_conta']
  extrato['tarifa'] = 0
  extrato['saldo'] =  cliente_new['valor_conta']
  extrato['data'] = f'{data.year} - {data.month} - {data.day} - {data.hour} - {data.minute}'

  with open('arquivo.json', 'r') as Extrato_Cliente:
    Cliente_Extract = json.load(Extrato_Cliente)

  Cliente_Extract.append(extrato)
    
  with open('arquivo.json', 'w') as Extrato_Cliente:
    json.dump(Cliente_Extract, Extrato_Cliente)
    
  print(Cliente_New)

def exclui_clientes():
  print()
  print('Você está em Apaga Cliente!')
  print()

  cpf = input("Digite seu CPF: ")
  senha = input("Digite sua senha: ")
  valor = float(input("Digite o valor: "))


  with open ("arquivo.json", "r") as f:
    clientes = json.load(f)
  
  
  for cliente in clientes:
    if cliente["cpf"] != cpf:
      clientes.append(cliente)

  print(clientes)
  
  with open("arquivo.json", "w") as f:
    json.dump(clientes, f)
    

  
def debito():
  print()
  print('Você está em Débito!')
  print()
  
  cpf = int(input("Digite seu CPF: "))
  senha = input("Digite sua senha: ")
  valor = float(input("Digite o valor a ser debitado: "))

  with open('arquivo.json', 'r') as f:
    clientes_debito = json.load(f)
    
  for cliente in clientes_debito:
    if cliente['cpf'] == cpf and cliente['senha'] == senha:
      cliente['valor_conta'] -= valor
      print(cliente)

  with open('arquivo.json', 'w') as f:
    json.dump(cliente, f)
    

  print(cliente)
  
def deposito():
  print()
  print('Você está em depósito!')
  print()
  
  cpf = int(input("Digite seu CPF: "))
  senha = input("Digite sua senha: ")
  valor = float(input("Digite o valor a ser debitado: "))

  with open('arquivo.json', 'r') as f:
    clientes_deposito = json.load(f)
    
  for cliente in clientes_deposito:
    if cliente['cpf'] == cpf and cliente['senha'] == senha:
      cliente['valor_conta'] += valor
      print(cliente)

  with open('arquivo.json', 'w') as f:
    json.dump(cliente, f)

  print(cliente)
  

def extrato():
  
  print()
  print('Você está em Débito!')
  print()
  
  cpf = input('Digite seu CPF: ')
  senha = input('Digite sua senha: ')
  ok = False
  with open('clientes.json', 'r') as f:
    clientes = json.load(f)
  for cliente in clientes:
    if cliente['cpf'] == cpf and cliente['senha'] == senha:
      ok = True
    elif ok:
      with open("extrato.json", "r") as f:
        extrato = json.load(f)
      for linha in extrato:
        if linha["cpf"] == cpf:
          print('Nome: ' + linha["nome"])
          print('CPF: ' + linha["cpf"])
          print('Tipo de Conta: ' + linha["conta"])
          print('Info: ' + linha["info"])
          print('Saldo Atual: ' + linha["saldo_atual"])
                  

def emprestimo():
  CPF = int(input("Digite seu CPF: ")) 
  compra = str(input('Digite o que irá comprar: '))
  valor = float(input(f'Digite o valor da/do {compra}: '))
  salario = float(input('Digite o seu salário: '))
  anos = int(input('Quantos anos para pagar: '))
  print()
  
  meses = anos * 12
  prestacao = valor / meses

  with open('arquivo.json', 'r') as f:
    clientes_emprestimo = json.load(f)
    
  for cliente in clientes_emprestimo:
    if cliente['cpf'] == CPF:
      if cliente['valor_conta'] < valor:
        if prestacao > salario * 0.3:
          print(f"Infelizmente você não pode obter o empréstimo, pois seu salario é R$ {salario} e o valor da sua conta é de {cliente['valor_conta']}, e a prestação é de R$ {prestacao:7.2f} .")
          print()
        else:
          print(f'Valor da prestação: R$ {prestacao:7.2f}. O Empréstimo está OK.')
          print()


  confirmacao = str(input(f"Deseja realizar o emprestimo com a prestacão de {prestacao:7.2f} a ser paga em {meses}? sim/não: "))
  if confirmacao == 'sim':
    print('Emprestimo deferido com sucesso.')
  else:
    print('Empestimo cancelado.')
