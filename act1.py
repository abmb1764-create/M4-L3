std={'s1':{"Name":"Jack", "Age":9, "Grade":4},     
     's2':{"Name":"brady", "Age":9, "Grade":4},
     's3':{"Name":"aarav", "Age":9, "Grade":4},
     's4':{"Name":"aarav", "Age":9, "Grade":4}}

name={}
result=[]
for i,details in std.items():
    uniqedata=(details['Name'], details['Age'], details['Grade'])
    if uniqedata not in result:
        result.append(uniqedata)
        name[i]=uniqedata

for i in name:
    print(i, ':',name[i])

