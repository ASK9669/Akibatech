# List of quiz questions, options, and correct answers
QUESTIONS = [
    {
        "question": "What is the capital city of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Pb", "C. Au", "D. Fe"],
        "answer": "C"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    }
]

def display_question(question_data, question_number):
    """Displays a single question and its options."""
    print(f"\nQuestion {question_number}: {question_data['question']}")
    for option in question_data['options']:
        print(option)

def validate_answer(user_input, valid_options):
    """Validates if the user input is among the allowed choices."""
    return user_input in valid_options

def check_answer(user_input, correct_answer):
    """Checks whether the user's answer is correct."""
    return user_input == correct_answer

def update_score(is_correct, score_tracker):
    """Updates the correct and incorrect answer counts based on performance."""
    if is_correct:
        score_tracker["correct"] += 1
        score_tracker["score"] += 1
    else:
        score_tracker["incorrect"] += 1
    return score_tracker

def calculate_category(percentage):
    """Calculates a performance category based on the final percentage."""
    if percentage == 100:
        return "🏆 Quiz Master! Absolute perfection!"
    elif percentage >= 80:
        return "🌟 Excellent Job! You know your stuff."
    elif percentage >= 60:
        return "👍 Good Effort! Solid understanding."
    elif percentage >= 40:
        return "📚 Not Bad, but room for improvement."
    else:
        return "💡 Keep Learning! Practice makes perfect."

def display_results(score_tracker, total_questions):
    """Displays the final score, percentage, breakdown, and result category."""
    correct = score_tracker["correct"]
    incorrect = score_tracker["incorrect"]
    score = score_tracker["score"]
    
    percentage = (score / total_questions) * 100
    category = calculate_category(percentage)
    
    print("\n" + "="*40)
    print("               QUIZ RESULTS               ")
    print("="*40)
    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {correct}")
    print(f"Incorrect Answers: {incorrect}")
    print(f"Final Score     : {score}/{total_questions}")
    print(f"Percentage      : {percentage:.2f}%")
    print(f"Performance     : {category}")
    print("="*40)

def play_quiz():
    """Runs a single instance of the quiz game."""
    score_tracker = {"score": 0, "correct": 0, "incorrect": 0}
    valid_options = ["A", "B", "C", "D"]
    total_questions = len(QUESTIONS)
    
    print("\n--- Welcome to the Command-Line Quiz Game! ---")
    print("Please type the letter corresponding to your choice (A, B, C, or D).\n")
    
    for idx, q_data in enumerate(QUESTIONS, start=1):
        display_question(q_data, idx)
        
        while True:
            user_input = input("Your answer (A/B/C/D): ").strip().upper()
            
            if validate_answer(user_input, valid_options):
                break
            print("❌ Invalid option! Please enter A, B, C, or D.")
            
        is_correct = check_answer(user_input, q_data['answer'])
        
        if is_correct:
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect! The correct answer was {q_data['answer']}.")
            
        update_score(is_correct, score_tracker)
        
    display_results(score_tracker, total_questions)

def main():
    """Main function to handle game loops and replayability without restarting Python."""
    while True:
        play_quiz()
        
        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()