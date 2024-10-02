import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a address and port
sock.bind(('localhost', 12345))

# Listen for incoming connections
sock.listen(5)

while True:
    # Accept incoming connections
    conn, addr = sock.accept()
    print('Connected by', addr)

    # Receive data from the client
    data = conn.recv(1024)
    print('Received:', data.decode())

    # Send data back to the client
    conn.sendall(b'Hello, client!')
    conn.close()