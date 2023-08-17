import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt \n")

    # TODO: Read database file into a variable

    db = []

    with open(sys.argv[1]) as file:
        reader_data = csv.DictReader(file)

        for row in reader_data:
            db.append(row)

    print(db)

    subsequence = list(db[0].keys())[1:]
    # print(subsequences)

    # TODO: Read DNA sequence file into a variable

    with open(sys.argv[2], 'r') as file:
        sequence = file.read()

    # print(sequence)

    # TODO: Find longest match of each STR in DNA sequence
    dna = []
    for i in range(len(subsequence)):
        number = longest_match(sequence, subsequence[i])
        dna.append(str(number))
    print(dna)

    # TODO: Check database for matching profiles

    is_found = False
    db_compare=[]
    for i in db:
        db_compare = list(db[i].keys())
        print(db_compare)
            # if db_compare == dna:
            #     is_found = True
            #     print(db["name"])

    # print("No match ")



    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
