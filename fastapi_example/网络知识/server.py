import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8090))

sock.listen(5)

while 1:
    conn, addr = sock.accept() # 阻塞等待客户端连接
    data = conn.recv(1024)
    print("客户端发送的请求数据: ", data)

    # conn.send(b"HTTP/1.1 200 ok\r\nserver:wangxin\r\n\r\nhello world")
    conn.send(b'HTTP/1.1 200 ok\r\nserver:wangxin\r\nContent-Type: application/json\r\n\r\n{"test": 1}')
    conn.close()
