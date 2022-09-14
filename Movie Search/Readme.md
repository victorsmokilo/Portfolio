An assignment from algorithm programming at my college:

# movies.py
I have a spreadsheet, permits.csv, which contains data about film permits issued by the city of New York (gently altered
from one obtained from NYC Open Data, https://opendata.cityofnewyork.us/).
Write a program that first creates a pandas Data Frame from this CSV file. The program should then allow the user to enter
a month and a year. The program should then report the zip code(s) that appear(s) most frequently in the ZipCode column
for rows with the given Month, the given Year, and with the EventType equal to Shooting Permit. Be aware that some rows
will have multiple entries in their ZipCode column: for these rows, each of the different ZipCode’s should be counted once.
I’d recommend using a dictionary to keep track of the counts.
Specifications: your program must
> Create a pandas Data Frame associated to the file permits.csv.

> Allow the user to input a month and a year.

> Report the zip code(s) that appear(s) most frequently in the ZipCode column for rows with the given Month, the given Year, and with the EventType equal to Shooting Permit.
