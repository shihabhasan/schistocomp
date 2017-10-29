import sys
import os
import subprocess
from Bio import SeqIO
import time


def getOrthologs(protFile1, protFile2):
    
    start_time = time.time()
    print("Orthlogous gene selection started...\n")
    print("Start Time:  "+str(time.asctime())+"\n")

            
    cline1 = "pb blastp -dbprot "+protFile1+" -query "+protFile2+" -out "+protFile1+"_"+protFile2+"_reciprocalBlast.txt -outfmt 10"
    return_code1 = subprocess.call(str(cline1), shell=(sys.platform!="linux"))
    print "Query: "+protFile2+"\n"+"Database: "+protFile1
    print "Reciprocal BLAST result saved to: "+protFile1+"_"+protFile2+"_reciprocalBlast.txt"

    cline2 = "pb blastp -dbprot "+protFile2+" -query "+protFile1+" -out "+protFile2+"_"+protFile1+"_reciprocalBlast.txt -outfmt 10"
    return_code2 = subprocess.call(str(cline2), shell=(sys.platform!="linux"))
    print "Query: "+protFile1+"\n"+"Database: "+protFile2
    print "Reciprocal BLAST result saved to: "+protFile2+"_"+protFile1+"_reciprocalBlast.txt"

    file1=open(protFile1+"_"+protFile2+"_reciprocalBlast.txt", "r")
    file2=open(protFile2+"_"+protFile1+"_reciprocalBlast.txt", "r")
    resultfile=open(protFile1+"_"+protFile2+"_orthologs.txt", "w")

    evalue = 0.00001
    perID = 70
    alignlenbp = 70

    myDict1={}
    mylist1=[]

    for line in file1:
        line=line.strip()
        l=line.split(",")
        if float(l[-2]) <= evalue and float(l[3]) >= alignlenbp and float(l[2])>= perID:
            if l[1] not in mylist1:
                myDict1.setdefault(l[0],l[1])#.split("|")[-1])
                mylist1.append(l[1])
    
    

    myDict2={}
    mylist2=[]
    for line in file2:
        line=line.strip()
        l=line.split(",")
        if float(l[-2]) <= evalue and float(l[3]) >= alignlenbp and float(l[2])>= perID:
            if l[1] not in mylist2:
                myList=myDict2.setdefault(l[0],l[1])#.split("|")[-1])
                mylist2.append(l[1])
            



    revDict2={}
    for key, val in myDict2.items():
        revDict2[val]=key



    reciDict={}
    for KEY,value in myDict1.items():
        if KEY in revDict2.keys():
            if revDict2[KEY]==value:
                reciDict.setdefault(KEY,value)

    file1.close()
    file2.close()
    print "Orthologs prediction completed"
    print "No. of best hit sequences from file1: "+str(len(myDict1.keys()))
    print "No. of best hit sequences from file2: "+str(len(myDict2.keys()))
    print "No. of orthologs: "+str(len(reciDict.keys()))

    orthoFasta=open(protFile1+"_"+protFile2+"_orthologs.fasta", "w")
    filtNovelFasta=SeqIO.index(protFile2,"fasta")

    for key,val in reciDict.items():
        resultfile.write(key+"\t"+val+"\n")
        orthoFasta.write(filtNovelFasta.get_raw(key))
    resultfile.close()
    orthoFasta.close()

    print "Orthologous gene list written to: "+protFile1+"_"+protFile2+"_orthologs.txt"
    print "Orthologous genes are written to: "+protFile1+"_"+protFile2+"_orthologs.fasta"      
    print "Finish Time:  "+str(time.asctime())
    print "Time elapsed:  "+str(time.time() - start_time)+"  seconds"
    print "--------------------------------------------------------------------------------------------------------\n"

protFile1 = str(sys.argv[1])
protFile2 = str(sys.argv[2])

getOrthologs(protFile1, protFile2)
