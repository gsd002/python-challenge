#import file
import os
import csv
election_csv=os.path.join("Resources","election_data.csv")

#lists to store data
ballot_id=[]
county=[]
candidate_list=[]

#read election_csv file:
with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader) #skip header
    for row in csvreader:
        #Add data to list
        ballot_id.append(row[0])
        county.append(row[1])
        candidate_list.append(row[2])

        #calculate total votes, candidate votes and percentage of votes
        total_votes = len(candidate_list)
        unique_candidates = list(set(candidate_list))
        vote_counts = [candidate_list.count(candidate) for candidate in unique_candidates]
        vote_percentages = [round((count / total_votes) * 100, 3) for count in vote_counts]

        #candidate with highest votes = winner
        max_votes = max(vote_counts)
        winner_index = vote_counts.index(max_votes)
        winner = unique_candidates[winner_index]

#Storing results in a dictionary
results_dict = {
    "Total Votes": total_votes,
    "candidates": [
        {
            "name": unique_candidates[i],
            "percentage": f"{vote_percentages[i]:.3f}%",
            "vote_count": f"({vote_counts[i]:,})"
        } for i in range(len(unique_candidates))
    ],
    "winner": winner
}
     
# converting the output as a list of strings and printing to terminal
results_output = [
    "Election Results",
    "------------------------------------------------",
    f"Total Votes: {results_dict['Total Votes']:,}",
    "------------------------------------------------",
]
results_output.extend([f"{candidate['name']}: {candidate['percentage']} {candidate['vote_count']}" for candidate in results_dict['candidates']])
results_output.append("-" * 42)
results_output.append(f"Winner: {results_dict['winner']}")
results_output.append("------------------------------------------------",)
print(results_output)

#set variable for output file
output_file=os.path.join("Analysis","analysis.txt")
#write the ouput file
with open(output_file,"w") as file:
    file.write('\n'.join(results_output))
