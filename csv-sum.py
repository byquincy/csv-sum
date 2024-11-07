import csv

DIR = "./csv.csv"
TARGET_ROW = 3

with open(DIR) as f:
    sigma = 0

    rdr = csv.reader(f)
    next(rdr)

    for line in rdr:
        sigma += float(line[TARGET_ROW])
    
    print(sigma)