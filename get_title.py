# output -> two files s_b_id_title.pickle, n_s_b_id_title.pickle
import re
id_title = {}

for i in xrange(1,4):
	fs = open("id_title_"+str(i))
	for line in fs:
		if re.match("id.*",line):
			continue
		else:
			temp = line.strip().split(";")
			if len(temp)>1:
				id_title[temp[0]] = temp[1]
	fs.close()

sb_id = []
n_sb_id = []

sb_id_title = {}
n_sb_id_title = {}

fs = open("../Sleeping_beauties_use.txt")

for line in fs:
	sb_id.append(line.strip())

fs.close()

fs = open("../Non_Sleeping_beauties_use.txt")

for line in fs:
	n_sb_id.append(line.strip())

fs.close()


for id_ in id_title:
	if id_ in sb_id:
		sb_id_title[id_] = id_title[id_]
	elif id_ in n_sb_id:
		n_sb_id_title[id_] = id_title[id_]
	else:
		continue

fs = open("s_b_id_title.pickle","w")

pickle.dump(sb_id_title,fs)

fs.close()

fs = open("n_s_b_id_title.pickle","w")

pickle.dump(n_sb_id_title,fs)

fs.close()
