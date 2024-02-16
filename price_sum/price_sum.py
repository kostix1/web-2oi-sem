import csv
def price():
    ctn1 = 0
    ctn2 = 0
    ctn3 = 0
    with open("./products.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ctn1 += float(row['Adult'])
            ctn2 += float(row['Pensioner'])
            ctn3 += float(row['Child'])
    print(round(ctn1, 2), round(ctn2, 2), round(ctn3, 2))
price()