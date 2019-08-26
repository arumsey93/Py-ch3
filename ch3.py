import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

#for number in range(1, 10):
  #  matching = False
    #for random in my_randoms:
       # if number == random:
          #  matching = True
    
   # print(f"List Contains Value: {matching, number}")

for number in range(1, 6):
    if my_randoms.count(number):
        print("List contains", number)
    else:
        print("List does not contain", number)
