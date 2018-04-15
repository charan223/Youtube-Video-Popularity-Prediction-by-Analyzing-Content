import re
import ast
import json
import xml.etree.ElementTree

ids = open("YT_BB_Validation_IDs.txt",'r').readlines()

f_ = open("incomplete_3.txt",'w')

#f2 = open("SleepingBeauties_Ids.txt",'r')

#f2_data = f2.read()

count = 0
count2 = 0
count1 = 0

for _id in ids:
    
    #if _id.strip('\n') in f2_data:
     #   continue
    
    x = _id.strip('\n')
    x = "daily_count_v/data/" + x[0] + "/" + x[1] + "/" + x[2] + "/" + x
    try:
        file_1 = open(x)
        
        count1 += 1

        data = xml.etree.ElementTree.fromstring(file_1.read())
        
        day = []
        daily_views = []
        
        for child in data:
            if child.tag == "graph_data":
                day = ast.literal_eval(re.findall("\"day\".*?\"data\".*?(\[.*?\])",child.text)[0])
                daily_views = ast.literal_eval(re.findall("\"daily\".*?\"data\".*?(\[.*?\])",child.text)[0])
        
        set_ = []
        set2 = []
        
        sum_ = 0
        count_ = 0
        
        for _x in xrange(1,len(day) - 1):
            if daily_views[_x] > daily_views[_x-1] and daily_views[_x] > daily_views[_x+1]:
                set_.append(daily_views[_x])
                set2.append(day[_x])
                sum_ += daily_views[_x]
                count_ += 1
        
        mean = 0
        
        if count_:
            mean = sum_/float(count_)
            
        SD = 0
        
        for _x in set_:
            SD += (_x - mean)*(_x - mean)
        
        if count_:
            SD = SD/float(count_)
        
        for _x,_y in zip(set_,set2):
            if _x > mean + SD:
                if _y - set2[0] > 31536000000 and _x > 70:
                    #print str(_id.strip("\n")) + ": Peak = " + str(_x)
                    f1 = open("Sleeping Beauties_3.txt",'a')
                    f1.write(str(_id))
                    f1.close()
                    count2 += 1
                    break
        
    except Exception,e:
        print str(_id) + " " + str(e)
        if "unclosed" in str(e):
            f_.write(str(_id))
        count += 1
    
f_.close()

print "Video not found: " + str(count)

print "Videos: " + str(count1)

print "Sleeping beauties: " + str(count2)
