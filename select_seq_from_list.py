from Bio import SeqIO
import sys


input_list_file=open(sys.argv[1],"r")

input_fasta=SeqIO.index(sys.argv[2],"fasta")

output_fasta=open(sys.argv[1]+"_filtered_from_"+sys.argv[2],"w")

for line in input_list_file:
    line=line.strip()
    if line in input_fasta.keys():
        output_fasta.write(">"+input_fasta[line].description+"\n"+str(input_fasta[line].seq)+"\n")
                    
                  

input_list_file.close()
output_fasta.close()
print 'DONE'

