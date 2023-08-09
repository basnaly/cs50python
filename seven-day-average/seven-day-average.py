import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):

    new_cases = dict()
    previous_cases = dict()

    for row in reader:
        state = row["state"]
        cases = row["cases"]
        if (state not in new_cases):
            new_cases[state] = []

        if (state not in previous_cases):
             new_daily_case = cases

        else:
            # print(state, cases, previous_cases[state])
            # print("----")
            new_daily_case = int(cases) - int(previous_cases[state])

        new_cases[state].append(new_daily_case)

        if len(new_cases[state]) > 14:
            new_cases[state].pop(0)

        previous_cases[state] = cases

    # print(new_cases)

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):

    week_data = new_cases[states[0]][7:]
    numerator = 

    print(week_data)

    try:
        numerator / denominator
    except ZeroDivisionError:


main()
