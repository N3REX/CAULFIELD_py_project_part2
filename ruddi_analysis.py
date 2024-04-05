#Caulfield PyProjectPt2

#Phase 3: Gnome analysis

#import/ant packages
from Bio import SeqIO
import pandas as pd
import os


# I mean it won't pull an input from the internet and use it, but at least this you can swap things out.
FileIthink = "GCA_000287275.1.fna"

rudtable = pd.DataFrame(columns =['Length', 'GC_Content', 'ATG_Forward', 'ATG_Reverse'])
pars = SeqIO.read(FileIthink, "fasta")


length  = len(pars.seq)
#There's some warning in the table construction step (FutureWarning) about Length being possibly NA?
if length == 0:
    print("Your fasta file is messed up and would bork up the analysis even if it went through >:(")
    os._exit()
gc_prop = ( ( (pars.seq.count("C")) + (pars.seq.count("G")) ) / length)*100
atg_fwd = (pars.seq.count("ATG"))
dwf_gta = (pars.seq.reverse_complement().count("ATG")) #get it? Its the REVERSE compliment


rudtable = pd.concat([rudtable, pd.DataFrame({ 'Length': length,
                                               'GC_Content': gc_prop,
                                               'ATG_Forward': atg_fwd,
                                               'ATG_Reverse': dwf_gta
                                             }, index=[0])], ignore_index=True)
rudtable.to_csv('ruddi.csv', index =False)

#This codeblock tried to flip the csv to look more like whats on the instructions (But I couldn't rename the row index values.
#rud_flip=rudtable.T 
#rud_flip.index = ['Length', 'GC_Content', 'ATG_Forward', 'ATG_Reverse'] #Didn't work
#rud_flip = rud_flip.rename(index={'Length': '1','GC_Content': '2','ATG_Forward': '3','ATG_Reverse': '4'})
#Both of these didn't work?
#rud_flip.to_csv('ruddi.csv', index =False)
