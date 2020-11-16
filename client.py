import socket

sock = socket.socket() #создаем сокет
sock.connect(('localhost', 9090)) #подключаемся к серверу

word = ''

while word != "exit":
    word = input("Input word > ") #вводим слово

    sock.send(bytes(word, encoding='UTF-8')) #шлем на сервер
    data = sock.recv(1024) #получаем результат
    print("Result: ",data.decode(),"\n") #выводим результат

sock.close()



