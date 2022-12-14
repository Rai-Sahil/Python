# Loop Control

# BREAK = terminates the loops completely.
while True:
    name = input("What is your name?")
    if len(name) != 0:
        break;


# PASS = Does nothing basically a place holder.
for i in range(1, 21):
    if i == 13:
        pass
    else: print(i)


# CONTINUE = skips to next iteration of the loop.
phone = "123-456-7890"

for i in phone:
    if i == "-":
        continue
    print(i, end = "")


