import os
import pandas as pd
import numpy as np
import sys

def selected_rows(group):
    sel_month = []
    sel_week = []
    for group_keys in group.groups:
        if group_keys[0] == 'Month':
            sel_month.append(group.get_group(group_keys).sample(n=8, random_state=13, axis=0))
        else:
            sel_week.append(group.get_group(group_keys).sample(n=6, random_state=13, axis=0))

    sel_week = pd.concat(sel_week)
    sel_month = pd.concat(sel_month)
    Block_df = pd.concat([sel_month, sel_week])
    return (Block_df)


if __name__ == "__main__":
    
    stim_list =  pd.read_csv ('Stim_' +(sys.argv[1])+'.csv')
    order_id=sys.argv[2]
    out_dir=f'Blocks/{(sys.argv[1])}_order{order_id}/'
    if not os.path.exists (out_dir):
        os.makedirs(out_dir)
    group = stim_list.groupby(by=['Category','distance','congruency', 'orientation'])
    sel = selected_rows(group)
    
    split_dfs = np.array_split(sel.sample(frac=1, random_state=20), 4)

# Print the split DataFrames
    for i, split_df in enumerate(split_dfs):
        split_df.to_csv(out_dir+f'Block {i+1}.csv')
        