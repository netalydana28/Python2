#Prison Break 

import numpy as np

prison = eval(input("Enter prison: "))

def set_free(prison):
    locked = 0
    unlocked = 1
    alt_prison = list()
    freed_prisoners = list()

    for i in range(len(prison)):
        if prison[i] == 0:
            alt_prison.append(1)
        elif prison[i] == 1:
            alt_prison.append(0)
    
    motion = True

    def clear_list(free):
        for i in range(free+1):
            prison.pop(0)
            alt_prison.pop(0)

    if prison[0] == 1:
        while (motion and 1 in prison) or ( not motion and 1 in alt_prison):

            if motion:
                free = prison.index(1)
                freed_prisoners.append(free)
                clear_list(free)
                motion = False
            else: 
                free = alt_prison.index(1)
                freed_prisoners.append(free)
                clear_list(free)
                motion = True

    return len(freed_prisoners)

print(set_free(prison))
