"""
####################################
i = 1

while i <= 10:
    print(i)
    i += 1

#####################################

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

##################################

i = 0
while i < 8:
    i += 1
    if i == 4:
        continue
    print(i)

##################################
"""

i = 1

while i < 5:
    print(i)
    i += 1
else:
    print("*" * 20)
    print(f"{i} não é menor que 5.")
    print("*" * 20)


