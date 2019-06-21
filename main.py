import os
import csv

data_csv = os.path.join("C:/Users/Josh Busser/Documents/GitHub/python-challenge1/03-Python_Homework_PyPoll_Resources_election_data.csv")

number_votes = 0
name = ""
name_votes = {}
name_percentages ={}
winner_votes = 0
winner = ""

# open csv file
with open(data_csv,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #  counting of votes
    for row in csvreader:
        number_votes = number_votes + 1
        name = row[2]
        if name in name_votes:
            name_votes[name] = name_votes[name] + 1
        else:
            name_votes[name] = 1

# calculate percentage and identify winner
for person, vote_count in name_votes.items():
    name_percentages[person] = '{0:.0%}'.format(vote_count / number_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

dashbreak = "-------------------------"

# print out results
print("Election Results")
print(dashbreak)
print(f"Total Votes: {number_votes}")
print(dashbreak)
for person, vote_count in name_votes.items():
    print(f"{person}: {name_percentages[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

# save summary to txt
save_file = data_csv.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write(dashbreak + "\n")
    text.write(f"Total Votes: {number_votes}" + "\n")
    text.write(dashbreak + "\n")
    for person, vote_count in name_votes.items():
        text.write(f"{person}: {name_percentages[person]} ({vote_count})" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write(dashbreak + "\n")