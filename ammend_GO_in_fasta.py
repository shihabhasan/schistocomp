from Bio import SeqIO
import sys

input_list_file=open(sys.argv[1],"r")

output_fasta=open(sys.argv[1]+"_modified_GO.fasta","w")

for line in input_list_file:
    line=line.strip()
    l=line.strip("\t")
    
    output_fasta.write(">"+input_fasta[line].description+"\n"+str(input_fasta[line].seq)+"\n")
                    
                  
input_list_file.close()
output_fasta.close()
print 'DONE'

