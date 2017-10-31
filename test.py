
import csv
data_row = csv.reader(open('./data/datat.csv'))
with open("output1.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(result_data)