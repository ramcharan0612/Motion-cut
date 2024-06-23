def run_quiz():
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"],
            "answer": "B"
        },
        {
            "question": "What year did the Titanic sink?",
            "options": ["A. 1905", "B. 1912", "C. 1921", "D. 1933"],
            "answer": "B"
        }
    ]
    
    score = 0
    
    print("QUIZ\n")
    print("Welcome to the Quiz!")
    print("Answer the following questions:")
    print("-----------------------------")
    
    for idx, question in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {idx}: {question['question']}")
        print("Options:")
        for option in question["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print("\nQuiz complete!")
    print(f"Your final score is {score}/{len(quiz_questions)}.\n")
    
    if score == len(quiz_questions):
        print("Congratulations! You answered all questions correctly.")
    elif score == 0:
        print("Better luck next time!")
    else:
        print("Well done! You did a good job.")

if __name__ == "__main__":
    run_quiz()
