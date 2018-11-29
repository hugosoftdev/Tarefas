from criar_instancia import create_instances

numberofinstances = None
while(not isinstance(numberofinstances, int)):
  try:
    numberofinstances = int(input('Quantas instancias deseja que seu server para tarefas tenha rodando ?: '))
  except:
    print('Inserir inteiro')
access_id = input('Qual o seu amazon access id ?: ')
secret_key = input('Qual a sua amazon secret key ?: ')
userData = """#!/bin/bash
  cd home/ubuntu/
  git clone https://github.com/hugosoftdev/load_balancer.git
  cd load_balancer/
  chmod +x install.sh
  echo {0} > number_of_instances.txt
  export AWS_ACCESS_KEY={1}
  export AWS_SECRET_KEY={2}
  ./install.sh
  """.format(numberofinstances,access_id,secret_key)
ip = create_instances(1, True, userData, access_id, secret_key)
ip = ip[0]
print('Load Balancer ID: ', ip)
with open("load_balancer_ip.txt", "w") as text_file:
    text_file.write(ip)
print('Seu programa de tarefas está pronto para uso, digite "python3 tarefas.py help" para saber seus comandos')
