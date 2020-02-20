import random

int rolls = input()
int roll = random.randint(0,5)
int 0roll = 0
int 1roll = 0
int 2roll = 0
int 3roll = 0
int 4roll = 0
int 5roll = 0

for(int i = 0; i < rolls; i++):
    roll
    if(roll=0):
        0roll+=1
    elif(roll=1):
        1roll+=1
    elif(roll=2):
        2roll+=1
    elif(roll=3):
        3roll+=1
    elif(roll=4):
        4roll+=1
    elif(roll=5):
        5roll+=1
        
print("you've rolled" + rolls + "times")
print("0: " + 0roll + "/" + rolls + " " + (0roll/rolls)*100 + "%")
print("1: " + 1roll + "/" + rolls + " " + (1roll/rolls)*100 + "%")
print("2: " + 2roll + "/" + rolls + " " + (2roll/rolls)*100 + "%")
print("3: " + 3roll + "/" + rolls + " " + (3roll/rolls)*100 + "%")
print("4: " + 4roll + "/" + rolls + " " + (4roll/rolls)*100 + "%")
print("5: " + 5roll + "/" + rolls + " " + (5roll/rolls)*100 + "%")


