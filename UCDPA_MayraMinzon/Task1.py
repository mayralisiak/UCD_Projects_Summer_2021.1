import pandas as pd
import re
from pathlib import Path

df = pd.read_csv(r"houses_data")
df.head()

searchlist = []
with open("houses_data.csv") as g:
    for line in g:
        searchlist.append(line.strip())

pattern = re.compile("Seatle".join(searchlist))
with open('houses_data.csv') as f:
    for line in f:
        if re.search(pattern, line):
            print(line)

#identity a pattern: find if the data contais the city Seatle
#with open(houses_data, 'r') as f_in:
    #with open(houses_data_Seatle, 'w') as f_outfile:
        #f_out = csv.writer(f_outfile)
        #for line in f_in:
            #line = line.strip()
            #row = []
            #if bool(re.search("Seatle", line)):
                #row.append(line)
                #f_out.writerow(row)
#df = pd.read_csv(houses_data_Seatle, header = None)
