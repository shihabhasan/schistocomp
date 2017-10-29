import sys
inFile=open(sys.argv[1], "r")
orthoFile=open(sys.argv[2], "r")

outFile=open(sys.argv[1]+"_combined_"+sys.argv[2], "w")
myList=[]
myDict={}
for line in inFile:
    line=line.strip()
    l=line.split(",")
    if l[0] not in myList:
        myDict[l[0]]=line
        myList.append(l[0])

inFile.close()

for line in orthoFile:
    line=line.strip()
    l=line.split(",")
    if l[0] in myDict.keys():
        outFile.write(line+","+myDict[l[0]]+"\n")
    

orthoFile.close()
outFile.close()
print "DONE"
