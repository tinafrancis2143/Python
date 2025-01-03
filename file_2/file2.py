file=open("file2.csv","r")
rows=file.readlines()
file.close()
file=open("file2result.csv","w")
file.write(rows[0])
for i in range(1,len(rows)):
    if(i%2==1):
        file.write(rows[i])

file.close()