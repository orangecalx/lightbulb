# grabs random bits of text from a given file
# variation 1 


import string
import random
fileout = open("output.txt", "w")
print("when you're ready to stop, press ctl-c")
sd = input("enter your favorite random number: ")
print("")

random.seed(sd)


try:

    while True:

        rand = random.randint(0, 2000)
        f = open('./corpus.txt', 'r', encoding="utf8")
        x = str(f.readline())
        y = x.split()
        z = random.choice(y)
        print(z, file=fileout)
        fil = str(z)
        fileout.write(fil)
        
        

except KeyboardInterrupt:
    pass
