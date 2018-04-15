
yes_count = 0
no_count = 0

yes = 0
i = 0

data = open('youtube_boundingboxes_detection_validation.csv').read()


for _line in open('allidsseparate'):

    y = _line.split(';')
    
    print i
    yes = 0
    if y[0] in data:
        yes_count += 1
        yes = 1
        f = open("Available3.txt","a")
        f.write(y[0] + "\n")
        f.close()
    if not yes:
        no_count += 1
    
    i += 1
print "Present: " + str(yes_count) + ", Absent: " + str(no_count)