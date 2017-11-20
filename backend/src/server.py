#!/usr/bin/python3
# -*- coding:utf-8 -*-

import socket
import json
from search import Search
from analyzer import Syntactic
from analyzer import Lexical

HOST = ''              # Endereco IP do Servidor
PORT = 5050            # Porta que o Servidor esta
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
socket_tcp.bind(orig)
socket_tcp.listen(1)
while True:
    print ('Servidor executando na porta {}'.format(PORT))
    client, addr = socket_tcp.accept()
    print ('Conectado por {}'.format(addr))
    while True:
        # Recebe claim
        claim_received = client.recv(4096).decode('utf-8')
        if not claim_received: break
        print ('Mensagem recebido do cliente: {}'.format(claim_received))

        # Criar list snippets
        snippets = []

        # Efetua busca por sininomos e sintatico
        print ('Executando léxico e buscando sinônimos...')
        words = Lexical(claim_received).analyze()
        print ('Executando sintático e construindo novas frases ...')
        claims = Syntactic(words).analyze()

        if claims:
            for claim in claims:
                print ('Buscando informações sobre: {}'.format(claim))
                snippets.append(Search().searchSnippet(claim))
                json_data = json.dumps(snippets)
        else:
            snippet_error = {}
            snippet_error['title'] = 'Error'
            json_data = json.dumps([snippet_error])
        # print ("JSON: {}".format(json_data))

        print ('Snippets enviados!')

        # Enviar snippets
        client.send(json_data.encode())
    print ('Finalizando conexao do cliente {}'.format(addr))
    client.close()