"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    def check_year(year):
        check = False
        if isinstance(year, str):
            try: 
                year = int(year[:4])
                if year>1886 and year<2014:
                    check = True
            except Exception as e:
                pass
        return check, year

    def check_uri(uri):
        return "dbpedia.org" in uri
        

    def writeToFile(filename, data):
        # This is just an example on how you can use csv.DictWriter
        # Remember that you have to output 2 files
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, delimiter=",", fieldnames= header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)


    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        g = []
        b = []

        for row in reader:
            check, year = check_year(row["productionStartYear"])
            if check_uri(row["URI"]):
                if check:
                    row["productionStartYear"]=year
                    g.append(row)
                else:
                    b.append(row)
        
        writeToFile(output_good, g)
        writeToFile(output_bad, b)

    #COMPLETE THIS FUNCTION

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()