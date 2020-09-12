#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticket_hash = {}
    output_list = []
    for ticket in tickets:
        ticket_hash[ticket.source] = ticket.destination
    current = ticket_hash["NONE"]
    output_list.append(current)
    while current != "NONE":
        output_list.append(ticket_hash[current])
        current = ticket_hash[current]

    print(ticket_hash)




    # Your code here

    return output_list



ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result) 
