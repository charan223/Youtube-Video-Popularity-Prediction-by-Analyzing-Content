import re
import ast
import json
import xml.etree.ElementTree
import pickle

def parse(fname):
	f = open(fname)
	data = xml.etree.ElementTree.fromstring(f.read())
	daily_views = []
	days = []
	for child in data:
		if child.tag == "graph_data":
			#day = ast.literal_eval(re.findall("\"day\".*?\"data\".*?(\[.*?\])",child.text)[0])
			daily_views = ast.literal_eval(re.findall("\"views\".*?\"data\".*?(\[.*?\])",child.text)[0])
			days = ast.literal_eval(re.findall("\"day\".*?\"data\".*?(\[.*?\])",child.text)[0])
	

	return daily_views,days


if __name__=="__main__":

	id_view_count = {}
	id_day_count = {}
	fs = open("you_tube_ids_separate")
	count_eli = 0
	count_n_eli = 0
	count_n_fnd = 0	
	cnt = 0
	
	for line in fs:
		d_c = []
		days = []
		flag = 0
		cnt +=1
		id_ = line.strip()
		#print "looking at",id_
		
		fname = "daily_count/data/"+id_[0]+"/"+id_[1]+"/"+id_[2]+"/"+id_
		try:
			d_c,days = parse(fname)
		except:
			flag =+1

		if flag==1:
			fname = "daily_count_v/data/"+id_[0]+"/"+id_[1]+"/"+id_[2]+"/"+id_
			try:
				d_c,days = parse(fname)
			except:
				flag+=1
		if flag==2:
			fname = "daily_count_3/data/"+id_[0]+"/"+id_[1]+"/"+id_[2]+"/"+id_
			try:
				d_c,days = parse(fname)
			except:
				flag+=1
		if flag==3:
			count_n_fnd +=1
			#print id_
			continue


		if len(d_c)>365:
			count_eli+=1
			id_view_count[id_] = d_c
			id_day_count[id_] = days
			#print len(id_view_count[id_]),len(id_day_count[id_])
		else:
			count_n_eli+=1
		
		print "processed",cnt
	fs.close()
	print "need to examine:",count_eli
	print "less than 1 year age:", count_n_eli
	print "not found:",count_n_fnd

	fs = open("daily_view_count.pickle","w")
	pickle.dump(id_view_count,fs)
	fs.close()

	fs = open("daily_day_count.pickle","w")
	pickle.dump(id_day_count,fs)
	fs.close()
	
	
'''
count = 0
count2 = 0
count1 = 0


f = open("021zNBkVCw4")
data = xml.etree.ElementTree.fromstring(f.read())
        
day = []
daily_views = []

for child in data:
    if child.tag == "graph_data":
        day = ast.literal_eval(re.findall("\"day\".*?\"data\".*?(\[.*?\])",child.text)[0])
        daily_views = ast.literal_eval(re.findall("\"views\".*?\"data\".*?(\[.*?\])",child.text)[0])
print daily_views
'''
#for _x in xrange(len(day)):
#	print daily_views[_x]
'''
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
'''
