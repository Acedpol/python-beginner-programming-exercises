import random

# ✅↓ Write your code here ↓✅
# r1 = random.randint(0, 10)
# print("Random number between 0 and 10 is %s" % (r1))

def generate_random():
    return random.randrange(9)

print(generate_random())