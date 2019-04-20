count = 1
counter = 1
max = 16
print(1)
while True:
    if (counter % 2 == 1 and (count + 9) > max):
        print(max)
        break
    if (counter%2==1):
        count +=9
    if (counter % 2 == 0):
        count -= 4
    print(count)
    counter += 1


