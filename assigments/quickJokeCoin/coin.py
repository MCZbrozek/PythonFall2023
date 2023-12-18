import random

print("Heads = Java is first, Tails = Data Science goes first ")

def flipCoin():
    side = random.randint(1,2)
    javaScore = 0
    dataScienceScore = 0
    for i in range (1, 10551):
        if (side == 1):
            result = "Heads"
            javaScore += 1
        else:
            result="Tails"
            dataScienceScore +=1
    if (javaScore > dataScienceScore):
        return f"Java goes first"
    else:
        return f"Data Science goes first"
    

result = flipCoin()
print(f"The coin has spoken\n", result)
