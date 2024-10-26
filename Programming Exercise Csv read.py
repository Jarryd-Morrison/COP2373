import csv

def read_and_display_csv():
    try:
        with open("grades.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            print(f"{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")
            print("=" * 60)
            
            for row in reader:
                # Display each row of data in a formatted manner
                print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")
    except FileNotFoundError:
        print("The file 'grades.csv' does not exist. Please ensure data has been entered.")

def main():
    read_and_display_csv()


main()
