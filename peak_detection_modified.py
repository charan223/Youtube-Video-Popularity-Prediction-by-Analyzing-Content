import pickle
import math


def IsSleepingBeauty(daily_views,_id):
	set_ = []
        set2 = []
        
        sum_ = 0
        count_ = 0
        
        for _x in xrange(1,len(daily_views) - 1):
            if daily_views[_x] > daily_views[_x-1] and daily_views[_x] > daily_views[_x+1]:
                set_.append(daily_views[_x])
                set2.append(_x)
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
	    SD = math.sqrt(SD)
        
        for _x,_y in zip(set_,set2):
            if _x > mean + SD:
                if _y - set2[0] > 365 and _x > 50:
                    #print str(_id.strip("\n")) + ": Peak = " + str(_x)
                    f1 = open("Sleeping_beauties_use.txt",'a')
                    f1.write(str(_id)+"\n")
                    f1.close()
		    return 1


	f1 = open("Non_Sleeping_beauties_use.txt","a")
	f1.write(str(_id)+"\n")
	f1.close()
        return 0            

	
if __name__=="__main__":
	fs = open("daily_view_count.pickle")
	id_view_count = pickle.load(fs)
	fs.close()

	s_b = 0
	n_s_b = 0

	print "files loaded"

	for key in id_view_count:
		print "looking at ",key
		a = IsSleepingBeauty(id_view_count[key],key)
		if a==1:
			s_b+=1
		else:
			n_s_b+=1
	print s_b,n_s_b
