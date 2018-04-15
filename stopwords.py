from nltk.corpus import stopwords

stops = stopwords.words("english")

print stops

f1 = open('likes_comments_categories/my_comments_remaining.csv','r')

f1_data = f1.readlines()

f2 = open('Sleeping Beauties.txt','r')
f2_data = f2.readlines()

f3 = open('NonSleepingBeauties_Ids.txt','r')
f3_data = f3.readlines()
print f3_data

Sleeping_beauties = 0

S_Sleeping_beauties = 0

Non_Sleeping_beauties = 0

S_Non_Sleeping_beauties = 0

i = 0

for x in f1_data:
    
    x = x.split(';')
    if str(x[0]+'\n') in f2_data:
        z = ''.join(i for i in x[1] if ord(i)<128)
        S_Sleeping_beauties += len(x[1])
        for y in stops:
            if y in z.lower():
                Sleeping_beauties += 1
    elif str(x[0]+'\n') in f3_data:
        z = ''.join(i for i in x[1] if ord(i)<128)
        S_Non_Sleeping_beauties += len(x[1])
        print x[1]
        for y in stops:
            if y in z:
                Non_Sleeping_beauties += 1
    print i
    i += 1

print "Sleeping beauties: " + str(Sleeping_beauties)

print "Non Sleeping beauties: " + str(Non_Sleeping_beauties)

print "Length"
print "Sleeping beauties: " + str(S_Sleeping_beauties/1138.0)

print "Non Sleeping beauties: " + str(S_Non_Sleeping_beauties/1138.0)