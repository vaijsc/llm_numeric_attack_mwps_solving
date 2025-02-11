from datasets import load_dataset

ds = load_dataset("lighteval/MATH", "algebra")['test']

ds_lv1 = [ds[i] for i in range(len(ds)) if ds[i]['level'] == 'Level 1']
ds_lv2 = [ds[i] for i in range(len(ds)) if ds[i]['level'] == 'Level 2']
ds_lv3 = [ds[i] for i in range(len(ds)) if ds[i]['level'] == 'Level 3']
ds_lv4 = [ds[i] for i in range(len(ds)) if ds[i]['level'] == 'Level 4']
ds_lv5 = [ds[i] for i in range(len(ds)) if ds[i]['level'] == 'Level 5']

lvs = list(set([ds[i]['level'] for i in range(len(ds))]))
print(ds[0])

print(lvs)

print(len(ds_lv1))
print(len(ds_lv2))
print(len(ds_lv3))
print(len(ds_lv4))
print(len(ds_lv5))
print(len(ds))