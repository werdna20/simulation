import random

def shuffle(arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i]

def deal():
    d=[]
    s=["♠","♥","♦","♣"]
    f={1:"A",11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d

###

cards = deal()
print("Before shuffle: ")
print(cards)

shuffle(cards)
print("After shuffle: ")
print(cards)
