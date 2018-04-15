from collections import Counter

f1 = open('Sleeping Beauties.txt','r')
f1_data = f1.readlines()

f2 = open('youtube_boundingboxes_detection_train.csv','r')
f2_data = f2.readlines()

f3 = open('SleepingBeauties_Ids.txt','r')
f3_data = f3.readlines()

f5 = open('NonSleepingBeauties_Ids.txt','w')

f4 = open('Common_Ids_YouTube_train_allidsseparate.txt','r')
f4_data = f4.readlines()

sleeping_beauties_objects = []
non_sleeping_beauties_objects = []

ids = []

i = 0

for x in f2_data:
    x = x.split(',')
    if str(x[0]+'\n') in f1_data:
        print x[0], x[3]
        sleeping_beauties_objects.append(x[3])
    elif i < 1138 and (str(x[0]+'\n') not in f3_data) and (str(x[0]+'\n') in f4_data):
        non_sleeping_beauties_objects.append(x[3])
        if x[0] not in ids:
            f5.write(x[0]+'\n')
            i = i + 1
            ids.append(x[0])

f5.close()

counter1 = Counter(sleeping_beauties_objects)
counter2 = Counter(non_sleeping_beauties_objects)

print "Sleeping Beauties" + str(counter1)

print "Non Sleeping Beauties" + str(counter2)