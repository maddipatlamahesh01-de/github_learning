#Deduplication of raw ids
raw_ids = [101, 102, 101, 103, 102, 104]
unique_ids=[]
ref=set()
for id in raw_ids:
    if id not in ref:
        unique_ids.append(id)
        ref.add(id)
print(unique_ids)