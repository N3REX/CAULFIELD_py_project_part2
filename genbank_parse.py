#Caulfield PyProjectPt2 

#Phase(?) 1: Genbank parsing

#import/ant packages
from Bio import SeqIO
import pandas as pd
import os

# List you could theoretically add stuff to and pull from
# (i.e. superscuffed futureproofing?)
accessionfiles = [
                  "NZ_CALPCP010000001.1.gb",
                  "NZ_CALPCY010000130.1.gb",
                  "NZ_BHVZ01000001.1.gb",
                  "NZ_SRYA01000017.1.gb",
                  "NZ_CAJTFZ010000019.1.gb"
                 ]

Table = pd.DataFrame(columns=['Accession', 'Family', 'Genus', 'Species', 'Num_Features', 'Source'])


for poor_nomenclature in accessionfiles: #cycle through
    pars = SeqIO.read(poor_nomenclature, "genbank") #Biopy "start"

    taxo = pars.annotations['taxonomy']
    family = taxo[-3]
    genus = taxo[-2]
    species = taxo[-1]
    num_features = len(pars.features)
    source = pars.annotations.get('source')
    accession = poor_nomenclature[:-3]
        # Staple the data
    Table = pd.concat([Table, pd.DataFrame({'Accession': accession,
                                        'Family': family,
                                        'Genus': genus,
                                        'Species': species,
                                        'Num_Features': num_features,
                                        'Source': source}, index=[0])], ignore_index=True)

Table.to_csv('genbank_parse.csv', index=False)