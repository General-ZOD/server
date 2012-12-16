import socket, threading, time;

def process_conn(connection, address):
    print "\nJust received a connection from", address;
    data_recvd = connection.recv(2048);
    print "Data received: \n", data_recvd;
    print "Going into sleep mode";
    time.sleep(60);
    print "waking up";
    data_sent = "Your data was well received,";
    connection.sendall(data_sent);
    connection.close();
    print "Just completed another request";

    
def main():
    HOST = "127.0.0.1";
    PORT = 20000;
    no_of_concurrent_connections = 2;

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    server.bind((HOST, PORT));
    server.listen(no_of_concurrent_connections);
    print "Waiting for clients to connect";
    while True:
        connection, address = server.accept();
        new_thread = threading.Thread(target=process_conn, args=(connection, address));
        new_thread.start();

if __name__ == "__main__":
    main();
