import numpy as np
import pandas as pd

CMP_COLUMNS = ['titleType', 'originalTitle', 'endYear', 'runtimeMinutes']

def is_duplicate(row_a, row_b, cols):
    row_a_without_nans = np.where(row_a[cols].isna(), 0, row_a[cols])
    row_b_without_nans = np.where(row_b[cols].isna(), 0, row_b[cols])
    return (row_a_without_nans == row_b_without_nans).all()

def deduplicate_group(group_info):
    _, group = group_info
    sorted_group = group.sort_values(by=CMP_COLUMNS, key=lambda x: x.isna())
    n_els = len(group)
    kept = set(range(n_els))
    for i in range(n_els):
        for j in range(i + 1, n_els):   
            if is_duplicate(sorted_group.iloc[i], sorted_group.iloc[j], cols=CMP_COLUMNS):
                kept.discard(j) 
    return sorted_group.iloc[list(kept)]