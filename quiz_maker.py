import random

def load_questions(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        questions = []
        temp_question = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Question"):
                if temp_question:
                    questions.append(temp_question)
                    temp_question = {}
                temp_question['question'] = line
            elif line.startswith("Answer:"):
                temp_question['answer'] = line.split(":")[1].strip()
            elif line:
                temp_question.setdefault('options', []).append(line)
        if temp_question:
            questions.append(temp_question)
    return questions

def create_quiz(questions, num_questions=5):
    random_questions = random.sample(questions, num_questions)
    return random_questions

def administer_quiz(quiz):
    score = 0
    for idx, question in enumerate(quiz, start=1):
        print(f"Question {idx}: {question['question']}")
        for i, option in enumerate(question['options'], start=97):  # ASCII code for 'a'
            print(f"{chr(i)}. {option}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == question['answer'].lower():
            score += 1
    return score

def main():
    questions_file = 'D:\EdYoda\quiz_maker\questions.txt'
    all_questions = load_questions(questions_file)
    
    num_questions_in_quiz = 10
      # Change this to set the number of questions in each quiz
    quiz = create_quiz(all_questions, num_questions_in_quiz)
    
    print("\nWelcome to the Quiz!")
    input("Press Enter to start the quiz...")
    print("\nQuiz Started!\n")
    
    user_score = administer_quiz(quiz)
    
    print(f"\nQuiz Finished! Your score: {user_score}/{num_questions_in_quiz}")
    
if __name__ == "__main__":
    main()
