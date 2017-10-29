from Bio import SeqIO
import sys

input_list_file=open(sys.argv[1],"r")

input_fasta=SeqIO.parse(sys.argv[2],"fasta")

output_fasta=open(sys.argv[1]+"_filtered_from_"+sys.argv[2],"w")

id_list=[]
for line in input_list_file:
    line=line.strip()
    id_list.append(line)

for record in input_fasta:
    if record.id not in id_list:
        output_fasta.write(">"+record.description+"\n"+str(record.seq)+"\n")
                  
input_list_file.close()
output_fasta.close()
print 'DONE'

