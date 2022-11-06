#Random string of specific letters

import random as r

specific_letters = ["A", "s", "B", "j", "V", "i", "C"] #my chosen specific letters
ans = ''.join(r.choice(specific_letters) for i in range(r.randint(1, 11))) #lenght of string is chosen randomly
print(ans)