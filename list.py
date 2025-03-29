import time
ticket_queue = [101, 102, 103, 104, 105]

while ticket_queue:
    current_ticket=ticket_queue.pop(0)
    print(f"Current ticket",current_ticket)
    time.sleep(4)
    if len(ticket_queue)<3:
        new_ticket=ticket_queue[-1]+1 if ticket_queue else 106
        ticket_queue.append(new_ticket)
        print(f"new customer",new_ticket)