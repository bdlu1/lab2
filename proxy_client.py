import socket
BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialize a socket, AF_INET => IPV4, SOCK_STREAM => TCP
    s.connect((host, port)) # connect to google
    s.send(request) # request google.com
    s.shutdown(socket.SHUT_WR) # im done sending the request. (Socket can write and socket can read) <- lets server know that you are
    # done writing the request so we shutdown the right side and get ready for receiving
    chunk = s.recv(BYTES_TO_READ) # continuously receiving the response
    result = b'' + chunk


    while(len(chunk)>0):
        chunk = s.recv(BYTES_TO_READ)
        result += chunk
    s.close()
    return result
        
print(get("127.0.0.1", 8080))