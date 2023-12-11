# To trim the FAM and HEX tags from the primers FAM: GAAGGTGACCAAGTTCATGCT   HEX: GAAGGTCGGAGTCAACGGAT


def read_csv(file_path):
    primers = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            primer_name, primer_sequence = row
            primers[primer_name] = primer_sequence
    return primers

def trim_sequence(tag_sequence, primers):
    trimmed_primers = {}
    for primer_name, primer_sequence in primers.items():
        trimmed_sequence = primer_sequence.replace(tag_sequence, '')
        trimmed_primers[primer_name] = trimmed_sequence
    return trimmed_primers

def export_results(trimmed_primers, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Primer Name', 'Trimmed Sequence'])
        for primer_name, trimmed_sequence in trimmed_primers.items():
            writer.writerow([primer_name, trimmed_sequence])

def main():
    # Assuming the CSV file is in the working directory
    csv_file_path = "KASP primers.csv"

    if not os.path.exists(csv_file_path):
        print(f"Error: The file {csv_file_path} does not exist.")
        return

    primers = read_csv(csv_file_path)

    tag_sequence = input("Enter the FAM sequence to remove: ")

    trimmed_primers = trim_sequence(tag_sequence, primers)

    # Export results to a new CSV file in the same directory as the script
    output_file_path = "FAM trimmed_results.csv"
    export_results(trimmed_primers, output_file_path)

    print(f"Results exported successfully to {output_file_path}.")

if __name__ == "__main__":
    main()

import os

def read_csv(file_path):
    primers = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            primer_name, primer_sequence = row
            primers[primer_name] = primer_sequence
    return primers

def trim_sequence(tag_sequence, primers):
    trimmed_primers = {}
    for primer_name, primer_sequence in primers.items():
        trimmed_sequence = primer_sequence.replace(tag_sequence, '')
        trimmed_primers[primer_name] = trimmed_sequence
    return trimmed_primers

def export_results(trimmed_primers, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Primer Name', 'Trimmed Sequence'])
        for primer_name, trimmed_sequence in trimmed_primers.items():
            writer.writerow([primer_name, trimmed_sequence])

def main():
    # Assuming the CSV file is in the working directory
    csv_file_path = "A1 trimmed_results.csv"

    if not os.path.exists(csv_file_path):
        print(f"Error: The file {csv_file_path} does not exist.")
        return

    primers = read_csv(csv_file_path)

    tag_sequence = input("Enter the HEX sequence to remove: ")

    trimmed_primers = trim_sequence(tag_sequence, primers)

    # Export results to a new CSV file in the same directory as the script
    output_file_path = "FAM and HEX trimmed_results.csv"
    export_results(trimmed_primers, output_file_path)

    print(f"Results exported successfully to {output_file_path}.")

if __name__ == "__main__":
    main()

import csv
def csv_to_fasta(csv_file, fasta_file):
    # Open CSV file and FASTA file
    with open(csv_file, 'r') as csv_file:
        with open(fasta_file, 'w') as fasta_file:
            # Create a CSV reader
            csv_reader = csv.reader(csv_file)

            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Extract primer name and sequence from each row
                primer_name, primer_sequence = row[0], row[1]

                # Write the FASTA entry to the FASTA file
                fasta_file.write(f'>{primer_name}\n{primer_sequence}\n')


# Replace 'input.csv' and 'output.fasta' with your actual CSV and FASTA file names
csv_to_fasta('FAM and HEX trimmed_results.csv', 'FAM and HEX trimmed_results.fasta')
