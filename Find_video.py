
yes_count = 0
no_count = 0

yes = 0
i = j = 0

f = open("Available.txt","w")

for _line in open('allidsseparate'):

    y = _line.split(';')
    
    print i, 
    j = 0
    for line in open('youtube_boundingboxes_detection_train.csv'):
        x = line.split(',')
        yes = 0
        print j,
        if x[0] == y[0]:
            yes_count += 1
            yes = 1
            f.write(x[0] + "\n")
            break
        j += 1
    if not yes:
        no_count += 1
    
    print ""
    i += 1
print "Present: " + str(yes_count) + ", Absent: " + str(no_count)