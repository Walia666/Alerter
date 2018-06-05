import csv

with open("new.csv", "wb") as fp:
          a = csv.writer(fp,delimiter=',')
          data=[['stock','sales'],
               ['100','24'],
               ['120','33']]
          a.writerows(data)