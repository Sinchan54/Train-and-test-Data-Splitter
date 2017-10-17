import random

fin = open("C:/Sinchan/object_recog/alscrap_train.txt", 'rb')
f75out = open("C:/Sinchan/object_recog/train_alscrap.txt", 'wb')
f25out = open("C:/Sinchan/object_recog/test_alscrap.txt", 'wb')
for line in fin:
    r = random.random()
    if r < 0.5:
        f75out.write(line)
    else:
        f25out.write(line)
fin.close()
f75out.close()
f25out.close()