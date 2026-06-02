import random


c = 0
while c < 5:
    coin = random.choice(["heads","tails"])
    print(coin)
    c = c+1