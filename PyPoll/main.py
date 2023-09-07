import os
import csv
pollcsv= os.path.join("Resources", "election_data.csv")


vote_count=0
#create dictionary to store unique values
unique_candidate_count={}



#read the file
with open(pollcsv, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csvheader=next(csvreader)

    for row in csvreader:
        #count the vote
        vote_count+=1

        candidate_name=row[2]

        if candidate_name in unique_candidate_count:
            unique_candidate_count[candidate_name] +=1

        else:
            unique_candidate_count[candidate_name]=1

#print(unique_candidate_count)
winner_candidate=max(unique_candidate_count, key=unique_candidate_count.get)

print("Election Results")
print("___________________________\n")

print(f"Total Votes: {vote_count}")

print("___________________________\n")

#print candidates and their vote share
for candidate, count in unique_candidate_count.items():
    vote_percentage= round(((count/vote_count)*100),3)

    print(f'{candidate}: {vote_percentage}% ({count})')

print("___________________________\n")

# print winner with max vote count

print(f'Winner: {winner_candidate}')


print("___________________________")      
      
#create output file
output_poll='poll_results.txt'

with open(output_poll,'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("___________________________\n")
    output_file.write(f"Total Votes: {vote_count}\n")
    output_file.write("___________________________\n")
    for candidate, count in unique_candidate_count.items():
        vote_percentage= round(((count/vote_count)*100),3)
        output_file.write(f'{candidate}: {vote_percentage}% ({count})\n')
    output_file.write('___________________________\n')
    output_file.write(f'Winner: {winner_candidate}\n')
    output_file.write('___________________________\n')

