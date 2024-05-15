#Jemell Rodgers
#4/30/2024
#P5HW

import random

def generate_question():
    """Generate a simple math
question."""

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.choice(['+', '-', '*'])
    if  operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"What is {num1} {operator} {num2}?"
    return question, answer


def main():
    """Main function to run the
quiz."""
    print("Welcome to the Simple Math Quiz!")
    score = 0
    num_questions = 5
    for _ in range(num_questions):
         question, correct_answer = generate_question()
         print(question)
         user_answer = int(input("Your answer: "))
         if user_answer == correct_answer:
            print("correct!")
            score += 1
         else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    print(f"You got {score}/ {num_questions} questions correct.")

if __name__ == "__main__":
    main()
                    
