import random

fin = open("Pathname/Main_Filename.txt", 'rb')
f1out = open("Pathname/Train_Filename.txt", 'wb')
f2out = open("Pathname/Test_Filename.txt", 'wb')
for line in fin:
    r = random.random()
    if r < 0.7:     #Change this value to decide the ratio you wanna split the files. I am doing it 70%-30%
        f1out.write(line)
    else:
        f2out.write(line)
fin.close()
f1out.close()
f2out.close()
