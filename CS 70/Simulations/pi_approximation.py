import random

trials = 100000



# Buffon's needle





# Square Dartboard
count = 0

for i in range(1, trials): 
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if x**2 + y**2 < 1:
        count += 1

print(f"Pi approximation from square dartboard: {4* count/trials}")



# Relatively prime integers

limit = 100000

count = 0

def relPrime(x, y) -> bool: 
    while y: 
        x, y = y, x % y
    if abs(x) == 1:
        return True
    else: 
        return False


for i in range(1, trials): 
    x = random.randint(1, limit)
    y = random.randint(1, limit)

    if relPrime(x, y):
        count += 1

print(f"Pi approximation from relatively prime integers: {(6/(count/trials))**(1/2)}")