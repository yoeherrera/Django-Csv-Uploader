import pandas as pd
import csv
from collections import defaultdict

def process_csv(input_filename, output_filename):
    # Open input and output files
    input_reader = pd.read_csv(input_filename)
    print(input_reader.head())
    output = input_reader.groupby(["Song","Date"]).agg('sum').rename(columns={'Number of Plays':'Total Number of Plays for Date'}).reset_index()
    return output

     # Save the new CSV file to a temporary file
    
    return response
    
def process_csv_by_line(input_filename, output_filename):
    # Open input and output files
    with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
        next(input_file)
        input_reader = csv.reader(input_file)
        output_writer = csv.writer(output_file)
        output_writer.writerow(["Song","Date","Total Number of Plays for Date"])
        # Use a defaultdict to keep track of the total number of plays for each song/date combination
        play_counts = defaultdict(int)
        # Iterate over each row in the input file and update the play counts
        for row in input_reader:
            song, date, num_plays = row
            play_counts[(song, date)] += int(num_plays)
        # Write the output file with the updated play counts
        for (song, date), total_plays in play_counts.items():
            output_writer.writerow([song, date, total_plays])
# if __name__ == "__main__":
#     import time
#     t0 = time.time()
#     print('processing csv ...')
#     filename = 'sample.csv'
#     process_csv(filename, 'try1.csv')
#     print('csv processed!')
#     t1 = time.time()
#     print(round(t1-t0,2), 'seg')