import socket
import json
from search import Search

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
        claim = client.recv(4096).decode('utf-8')
        if not claim: break
        print ('Mensagem recebido do cliente: {}'.format(claim))

        # Criar list snippets
        snippets = []
        
        # Efetua busca
        # Adiciona sinppet na lista
        print ('Construindo Snippet 1...')
        snippets.append(Search().searchSnippet(claim))
        print ('Construindo Snippet 2...')
        snippets.append(Search().searchSnippet(claim + ' 2'))
        print ('Construindo Snippet 3...')
        snippets.append(Search().searchSnippet(claim + ' 3'))

        # Adiciona lista no json
        json_data = json.dumps(snippets)
        # print ("JSON: {}".format(json_data))

        print ('Snippets enviados!')

        # Enviar snippets
        client.send(json_data.encode())
    print ('Finalizando conexao do cliente {}'.format(addr))
    client.close()