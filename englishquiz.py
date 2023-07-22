import random

# Quiz Questions
quiz_questions = [
    {
        "question": "What is the past tense of 'go'?",
        "choices": ["A. Went", "B. Gone", "C. Goed", "D. Going"],
        "answer": "A. Went"
    },
    {
        "question": "Choose the correct spelling: ",
        "choices": ["A. Recieve", "B. Receive", "C. Recievee", "D. Receeve"],
        "answer": "B. Receive"
    },
    {
        "question": "What is a synonym for 'happy'?",
        "choices": ["A. Sad", "B. Angry", "C. Joyful", "D. Tired"],
        "answer": "C. Joyful"
    },
    {
        "question": "Which word means 'a small piece of paper that proves you have paid for something'?",
        "choices": ["A. Receipt", "B. Invoice", "C. Coupon", "D. Voucher"],
        "answer": "A. Receipt"
    },
    {
        "question": "What is the opposite of 'extrovert'?",
        "choices": ["A. Shy", "B. Friendly", "C. Outgoing", "D. Introvert"],
        "answer": "D. Introvert"
    }
]

# Function to load a random order of questions
def get_random_question_order():
    return random.sample(range(len(quiz_questions)), len(quiz_questions))

# Function to present the quiz questions
def present_quiz_questions():
    score = 0
    question_order = get_random_question_order()
    for i in range(len(quiz_questions)):
        question_index = question_order[i]
        question = quiz_questions[question_index]
        print(f"\nQuestion {i+1}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        user_answer = input("Enter your answer (e.g., A, B, C, D): ")
        if user_answer.lower() == question['answer'][0].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question['answer']}")
    return score

# Display welcome message and rules
print("Welcome to the Quiz Game!")
print("You will be presented with multiple-choice questions.")
print("Choose the correct answer by typing the corresponding letter.")
print("Let's get started!")

play_again = True
while play_again:
    # Present quiz questions
    score = present_quiz_questions()

    # Calculate final score
    total_questions = len(quiz_questions)
    percentage = (score / total_questions) * 100

    # Display final results
    print("\n--- Quiz Results ---")
    print(f"You scored {score} out of {total_questions} questions. ({percentage}%)")
    if percentage == 100:
        print("Congratulations! You got a perfect score!")
    elif percentage >= 75:
        print("Well done! You did a great job!")
    elif percentage >= 50:
        print("Not bad! Keep improving!")
    else:
        print("Better luck next time!")

    # Ask the user if they want to play again
    play_again_input = input("Do you want to play again? (yes/no): ")
    play_again = play_again_input.lower() == "yes"
