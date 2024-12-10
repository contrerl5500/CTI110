# Ask user for the number of scores they would like to enter
num_scores = int(input("How many scores do you want to enter? "))

# Initialize an empty list to store valid scores
scores = []

# Loop to collect each score
for i in range(num_scores):
    score = -1  # Initialize with an invalid score
    while score < 0 or score > 100:
        score_input = input(f"Enter score #{i + 1}: ")
        if score_input.replace('.', '', 1).isdigit():  # Check if the input is a valid number
            score = float(score_input)
            # Check if score is within the valid range
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("INVALID Score entered! Score should be between 0 and 100")
        
# Lowest score entered
lowest_score = min(scores)

# Remove the lowest score from the list
modified_scores = scores.copy()
modified_scores.remove(lowest_score)

# Calculate the average of the modified list
if modified_scores:
    average_score = sum(modified_scores) / len(modified_scores)
    
# Determine the letter grade
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

# Display results
print("----------------------Results---------------------------")
print(f"{"Lowest Score":<10} {lowest_score}")
print(f"{"Modified List":<10} {modified_scores}")    
print(f"{"Scores Average":<10} {average_score:.2f}")
print(f"{"Grade":} {grade}")
print("------------------------------------------------------")
