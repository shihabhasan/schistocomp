import sys

inFileName=sys.argv[1]

inFile=open(inFileName, "r")

outFile=open(inFileName+"_arranged.csv", "w")


myDict={}
myList=[]
for line in inFile:
    line=line.strip()
    l=line.split("\t")
    v=l[2]+","+l[1]+","+l[4]+","+l[8]+","+l[9]

    myList=myDict.setdefault(l[2],[])
    if v not in myList:
        myList.append(v)


for key in myDict:
    outFile.write(str(myDict[key])+"\n")

inFile.close()
outFile.close()


print "JOB DONE!!!!"
