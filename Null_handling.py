#Remove the Null values and filter salary > 30000

records = [
    {"id": 1, "salary": 25000},
    {"id": 2, "salary": None},
    {"id": 3, "salary": 45000},
    {"id": 4, "salary": 32000}
]
clean_record=[]
for record in records:
    salary=record["salary"]
    if salary is not None and salary>30000:
        clean_record.append(record)
print(clean_record)