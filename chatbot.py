import os

def processar_resposta(resposta, name):
  if resposta == '1':
    print(f'{os.linesep}{name}, Python é divertido!{os.linesep}')
  elif resposta == '2':
    print(f'{os.linsep}{name}, Estudando conceitos básicos primeiro e depois vai avançando.{os.linesep}')
  elif resposta == '3':
    print(f'{os.linesep}{name}, Estudando blibiotecas como (os, random e muitas outras).{os.linesep}')
  else:
    print(f'Opção nválida. Tente novamente.')
  
def iniciar():
  name = input('Digite seu nome: ')
  email = input('Digite seu e-mail: ')
  while True:
    resposta = input(f'{os.linesep}[1] - Como é a linguagem Python?{os.linesep}
    {os.linesep}[2] - Como aprender Python?{os.linesep}
    {os.linsep}[3] - Como  criar bot em Pyhton?{os.linesep}')
    processar_resposta(resposta, nome)
    
if __name___ == "__main__":
  start()
