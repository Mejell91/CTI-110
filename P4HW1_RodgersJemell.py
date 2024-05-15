#Jemell Rodgers
#March 29 2024
#P4HW1
#ScoreList
scores = []
num_scores = int(input("How many scores do you want to enter? "))

for num_1 in range(1, num_scores + 1):
    score = float(input(f"Enter score #{num_1}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{num_1} again: "))
    scores.append(score)



lowest_score = min(scores)
modified_list = [score for score in scores if score != lowest_score]
average_score = sum(modified_list) / len(modified_list)

print("--------Results--------")
print("Lowest Score:", lowest_score)
print("Modified List:", modified_list)
print("Scores Average:{:.2f}".format(average_score))

if average_score >= 90:
    print("Grade: A")
elif average_score >= 80:
    print("Grade: B")
elif average_score >= 70:
    print("Grade: C")
elif average_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
      

    
        
