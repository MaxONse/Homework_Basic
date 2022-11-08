clients = ['Jim', 'John', 'Nick', 'Jim', 'Mike', 'John', 'Doe', 'Michael', 'Jim', 'Jack', 'John']
requestedClient = 'Jim'
def request():
    position = clients.count(requestedClient)
    print("Numbers of positions in list: ", position)
    while requestedClient in clients:
        index = clients.index(requestedClient)
        print("Position is: ", index+1)
        clients[index] = ''
    if position > 1:
        print("He is regular customer, there is a discount")
request()