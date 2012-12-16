import socket;

def main():
    HOST = "127.0.0.1";
    PORT = 20000;

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print "Connecting to host now";
    try:
        client.connect((HOST, PORT));
        print "Sending data to server now";
        data_sent = "tis the season to be jolly";
        client.sendall(data_sent);
        data_recvd = client.recv(2048);
        print "Response received: ", data_recvd;
        client.close();
    except Exception, e:
        print e;
    

if __name__ == "__main__":
    main();
