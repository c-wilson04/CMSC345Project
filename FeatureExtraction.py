import numpy as np
import pandas as pd
import Bio
import re

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def clean_data(data: pd.DataFrame, substitute=False) -> pd.DataFrame:
    """Replace abiguous amino acids with either nothing or map them to known acids."""
    data = data.copy(deep=True)
    mappings = str.maketrans({
        'B': 'D',
        'Z': 'E',
        'J': 'L',
        'U': 'C',
        'O': 'K',
        'X': 'G'
    })
    if substitute:
        data['protien_seq'] = data['protien_seq'].apply(lambda x: x.translate(mappings))
    else:
        data['protien_seq'] = data['protien_seq'].apply(lambda x: re.sub('[BZJUOX]', '', x))
    return data



def extract_features(data: pd.DataFrame) -> pd.DataFrame:
    """Takes in a pandas dataframe containing all of the protien sequences and class labels, and returns a dataframe with features extracted from biopython."""
    data = data.copy(deep=True)
    # create objects for biopython analysis

    data["protien_len"] = data["protien_seq"].apply(len)
    
    
    data["protien_an"] = data["protien_seq"].apply(ProteinAnalysis)
    
    data["mol_weighht"] = data["protien_an"].apply(lambda x: x.molecular_weight())
    data["isoelectric_point"] = data["protien_an"].apply(lambda x: x.isoelectric_point())
    data["isoelectric_point"] = data["protien_an"].apply(lambda x: x.gravy())

    secondary_struct = pd.DataFrame(list(data["protien_an"].apply(lambda x: x.secondary_structure_fraction())), columns=["Helix", "Turn", "Sheet"])
    data = pd.concat([data, secondary_struct], axis=1)

    # count protien types
    acid_count = data["protien_an"].apply(lambda x: x.count_amino_acids()).apply(pd.Series)
    data["type1"] = acid_count[['A', 'G', 'I', 'L', 'M', 'F', 'P', 'W', 'V']].sum(axis=1)
    data["type2"] = acid_count[['S', 'C', 'N', 'Q', 'T', 'Y']].sum(axis=1)
    data["type3"] = acid_count[['D', 'E']].sum(axis=1)
    data["type4"] = acid_count[['K', 'R', 'H']].sum(axis=1)

    acid_perc = data["protien_an"].apply(lambda x: x.amino_acids_percent).apply(pd.Series)
    data = pd.concat([data, acid_perc], axis=1)

    data["pos_neg_rat"] = data["type4"] / (data["type3"] + 0.00001)

    # drop uneeded values

    data = data.drop(['protien_seq', 'protien_an'], axis=1)
    return data
    