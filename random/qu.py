import csv

f = open("migration.csv")
w = open("wrapper.sql", "w")
reader = csv.reader(f)
for row in reader:
    w.write("INSERT INTO sd_ims_eligible_number_prefixes VALUES ('" + row[0] + "', 1);\n")
f.close()
w.close()
