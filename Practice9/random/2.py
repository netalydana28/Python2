"""
Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
Note you must adhere to the following conditions:
•	The lottery number must be 10 digits long.
•	All 100 ticket number must be unique.

"""

import random as r

tickets_set = set()

while len(tickets_set) != 100 :
    a = r.randint(1000000000, 10000000000)
    tickets_set.add(a)

tickets_set = list(tickets_set)

lucky_tickets = list()

while len(lucky_tickets) != 2:
    temp = r.choice(tickets_set)
    lucky_tickets.append(temp)

print(f"Lucky ticket: {lucky_tickets[0]}, {lucky_tickets[1]}\n")

print("Tickets:\n")

for i in range(len(tickets_set)): #Here i print out list of tickets, where lucky tickets will be marked
    if tickets_set[i] in lucky_tickets:
        print(f"{tickets_set[i]} <-- Lucky ")
    else:
        print(tickets_set[i])


