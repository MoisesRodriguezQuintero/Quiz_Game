from UpdateScore import update_score
from CalculatePercentage import calculate_percentage
from CheckAnswer import check_answer
from ManageQuestions import manage_questions, questions
from ShowFinalResult import show_final_result
from ShowQuestion import show_question


def ask_number(max_option: int) -> int:
    # Repite la pregunta hasta que el usuario escriba un número válido
    while True:
        try:
            answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if 1 <= answer <= max_option:
            return answer
        print(f"Please choose a number between 1 and {max_option}.")


def main() -> None:
    score = 0
    selected_questions = manage_questions(questions, 3)
    total_questions = len(selected_questions)

    for q in selected_questions:
        show_question(q["question"], q["answers"])
        user_answer = ask_number(len(q["answers"]))
        result = check_answer(user_answer, q["correct"])

        if result:
            print("Correct!")
        else:
            print("Wrong! The correct answer was:", q["answers"][q["correct"] - 1])

        score = update_score(score, result)

    percentage = calculate_percentage(score, total_questions)
    show_final_result(score, total_questions, percentage)


if __name__ == "__main__":
    main()
