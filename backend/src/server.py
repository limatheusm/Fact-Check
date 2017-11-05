import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5050            # Porta que o Servidor esta
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
socket_tcp.bind(orig)
socket_tcp.listen(1)
while True:
    client, addr = socket_tcp.accept()
    print ('Concetado por {}'.format(addr))
    while True:
        claim = client.recv(4096)
        if not claim: break
        print ('Mensagem recebido do cliente: {}'.format(claim.decode('utf-8')))
        client.send(claim)
    print ('Finalizando conexao do cliente {}'.format(addr))
    client.close()