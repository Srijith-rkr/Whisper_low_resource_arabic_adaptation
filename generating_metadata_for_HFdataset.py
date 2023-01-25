import os
import pandas as pd

df = pd.DataFrame( columns=['file_name','class','split'])


for split in os.listdir('data'):
    for class_ in os.listdir('data/'+split):
        for file_name in os.listdir(os.path.join('data',split,class_)):
            new_row = {}
            new_row['file_name'] = os.path.join('data',split,class_,file_name)
            new_row['class'] = class_
            new_row['split'] = split
            df = df.append(new_row, ignore_index=True)
            
df.to_csv('metadata.csv',index=False)
            
# from datasets import load_dataset
# dataset = load_dataset("audiofolder", data_dir="data")