a = 9000000000 #initiate the count.
b = 9999999999 #last instance
for i in range(a,b):
    a = a+1
    print(a)
    list = [int(d) for d in str(a)] #convert number into list
    count = 0
    flag = 0
	#To eleminate number with repeatation of certain digit more than 5 times
    for i in range(len(list)):
        if count==5:
            flag =1
            break
        else:
            count =0
        for j in range(1,len(list)):
            if list[i]==list[j]:
                count=count+1
    if flag == 1:
        continue
    else:
	#To write your wordlist in the worlist file.
        f = open("wordlist.txt","a")
        f.write(str(a))
        f.write(str("\n"))
f.close()
