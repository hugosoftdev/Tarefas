#!/usr/bin/env python3
import sys
import requests
import os

f = open('./load_balancer_ip.txt')
ip = f.readline()
f.close()
API_PATH =  "http://{0}:8888/task".format(ip)


def help():
  text = """
      Seguem os comando seguidos de seus possíveis argumentos:
      listar
      adicionar <nome_da_tarefa>
      buscar <id_da_tarefa>
      apagar <id_da_tarefa>
      atualizar <id_da_tarefa> <novo_nome_da_tarefa>
      help 
        """
  print(text)

def listar():
  print(requests.get(API_PATH).text)

def adicionar():
  if(len(arguments) < 3):
    return help()
  print(requests.post(API_PATH, json={"value": arguments[2]}).text)

def buscar():
  if(len(arguments) < 3):
    return help()
  print(requests.get(API_PATH+"/{0}".format(arguments[2])).text)

def apagar():
  if(len(arguments) < 3):
    return help()
  print(requests.delete(API_PATH+"/{0}".format(arguments[2])).text)

def atualizar():
  if(len(arguments) < 4):
    return help()
  print(requests.put(
      API_PATH+"/{0}".format(arguments[2]), json={"value": arguments[3]}).text)
  

global arguments
arguments = sys.argv

valid_commands = ['listar','adicionar','buscar','apagar', 'atualizar','help']


if(len(arguments) == 1):
  help()
elif(arguments[1] not in valid_commands):
  help()
else:
  try:
    locals()[arguments[1]]()
  except:
     e = sys.exc_info()[0]
     print("Error: {0}".format(e))
