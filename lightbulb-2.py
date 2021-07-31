# grabs random bits of text from a given file
# variation 2



import string
import random
import time

fileout = open("output.txt", "w")
print("")
print("output will be saved to 'output.txt' upon stopping")
print("")
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
        nl = random.randint(0, 4)
        s = ""

        if nl == 2:
            s = "\n"
        else:
            pass

        print(".")
        print(z, s, end="", file=fileout)

        time.sleep(.01)


except KeyboardInterrupt:
    pass


