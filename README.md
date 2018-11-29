# Tarefas
## Um projeto overkill para gerenciar tarefas pelo terminal

dependencias: boto3, aws account, firebaseDB account

Com apenas um comando: python3 init.py

você configura uma baita de uma infraestrutura na amazon para que seu gerenciamento de tarefas nunca falhe.

funcionalidades:
  - Load Balancing
  - HA, healthchecks que garantem que o número de instancias desejadas estejam sempre disponíveis
  - Stateless (usando Firebase no webserver)
  - Número de instancias configuravel
  


