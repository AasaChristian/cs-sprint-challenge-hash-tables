#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    hash = {}
    route = []

    for x in tickets:
        hash[x.source] = x.destination

    route.append(hash['NONE'])
    while hash[route[-1]] != 'NONE':
        route.append(hash[route[-1]])
    route.append('NONE')

    

     





    return route



# tickets = [
#     Ticket( "PIT",  "ORD") ,
#     Ticket( "XNA",  "CID" ),
#     Ticket( "SFO",  "BHM" ),
#     Ticket( "FLG",  "XNA" ),
#     Ticket( "NONE",  "LAX" ),
#     Ticket( "LAX",  "SFO" ),
#     Ticket( "CID",  "SLC" ),
#     Ticket( "ORD",  "NONE" ),
#     Ticket( "SLC",  "PIT") ,
#     Ticket( "BHM",  "FLG") 
# ]

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
print(reconstruct_trip(tickets, 10))