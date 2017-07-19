import sys
from Bio import SeqIO

def split_fasta(multifasta):
    with open(multifasta, 'r') as infile:
        records = SeqIO.parse(infile, 'fasta')
        for record in records:
            filename = record.id + '.fa'
            out_handle = open(filename, 'w')
            SeqIO.write(record, out_handle, 'fasta')
            out_handle.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
         split_fasta(sys.argv[1])
    else:
         print("Usage: split_fasta.py multifasta.fa blargh")
         sys.exit(0)
