#Caulfield PyProjectPt2

#Phase(?) 2: Protein fasta stuff

#import/ant packages
from Bio import SeqIO
import pandas as pd
import os


# These parts seem on paper pretty similar aside from the actual chart content, so may as well just retool the first script.
protfile = [
            "AGI40145.1.fasta",
            "AGJ87295.1.fasta",
            "WVV45440.1.fasta",
            "WVS05366.1.fasta"
           ]

protable = pd.DataFrame(columns =['ID', 'First_10_AA', 'Length', 'Number_Cs'])


for poor_nomenclature in protfile: #cycle through
    pars = SeqIO.read(poor_nomenclature, "fasta") 
    ego = str(pars.id)
    batteries = (str((pars.seq)[0:10]))
    width = len(pars.seq)
    scurvy = (pars.seq.count("C"))
        # Staple the data
    protable = pd.concat([protable, pd.DataFrame({'ID': ego,
                                                  'First_10_AA': batteries,
                                                  'Length': width,
                                                  'Number_Cs': scurvy
                                                 }, index=[0])], ignore_index=True)
        
protable.to_csv('Protein_Table.csv', index =False)
