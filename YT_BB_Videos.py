# f1 = open('youtube_boundingboxes_detection_train.csv','r')
# f1_data = f1.readlines()
# 
# f3 = open('YT_BB_Train_IDs.txt','w')
# 
# ids = []
# 
# i = 0
# 
# for x in f1_data:
#     x = x.split(',')
#     if x[0] not in ids:
#         ids.append(x[0])
#         f3.write(x[0]+'\n')
#     print i
#     i += 1
# 
# f3.close()
# 
# f1.close()

f2 = open('youtube_boundingboxes_detection_validation.csv','r')
f2_data = f2.readlines()

f3 = open('YT_BB_Validation_IDs1.txt','w')

ids = []

i = 0

for x in f2_data:
    x = x.split(',')
    if x[0] not in ids:
        ids.append(x[0])
        f3.write(x[0]+'\n')
    print i
    i += 1

f3.close()

f2.close()