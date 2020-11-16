import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()  # подключаем client

print('connected:', addr)

# словарь
dictionary = {"doctor": "a qualified practitioner of medicine; a physician.",
              "driver": "a person who drives a vehicle.",
              "cup": "a small bowl-shaped container for drinking from, typically having a handle.",
              "keyboard": "a panel of keys that operate a computer or typewriter.",
              "mouse": "a small rodent that typically has a pointed snout, relatively large ears and eyes, and a long tail.",
              "cross": "a mark, object, or figure formed by two short intersecting lines or pieces (+ or ×).",
              "search": "try to find something by looking or otherwise seeking carefully and thoroughly",
              "dice": "play or gamble with dice.",
              "python": "a high-level general-purpose programming language.",
              "server": "a computer or computer program which manages access to a centralized resource or service in a network."}

while True:
    data = conn.recv(1024)  # получаем слово
    if not data:  # если нет данных
        break

    data = data.decode().replace('\n', '')  # декодируем

    data = dictionary.get(data)  # получаем значение по словарю

    if data == None:  # если значения нет, то записываем в объект слово ОШИБКА
        data = "Error"

    conn.send(bytes(data, encoding='UTF-8'))  # отправляем ответ клиенту

conn.close()
