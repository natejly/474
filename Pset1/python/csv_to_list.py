import csv

def csv_to_list(input_csv, output_txt):
    # Read CSV and convert to a list of lists
    csv_list = []
    with open(input_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_list.append(row)
    
    # Write the Python list to a text file
    with open(output_txt, 'w') as file:
        file.write("csv_list = [\n")
        for row in csv_list:
            file.write(f"    {row},\n")
        file.write("]\n")
        
if __name__ == "__main__":
    csv_to_list("crib.csv", "chart.txt")