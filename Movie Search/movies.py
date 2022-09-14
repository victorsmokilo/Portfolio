

import pandas as pd

permits_df = pd.read_csv('permits.csv')


zipcodes = {}

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))


for i in range(len(permits_df['EventID'])):
    if permits_df.at[i,'Month'] == month and permits_df.at[i,'Year'] == year and permits_df.at[i,'EventType'] == 'Shooting Permit':
        x = permits_df.at[i,'ZipCode'].split()
        for a in range(len(x)):
            try:
                zipcodes[x[a]] += 1
            except KeyError:
                zipcodes[x[a]] = 1
                
x = max(zipcodes, key=zipcodes.get)
print(max(zipcodes, key=zipcodes.get), zipcodes[x])














































































