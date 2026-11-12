def show_final_result(score, total_questions, percentage):
    print("\n===== FINAL RESULT =====")
    print("Your score:", score)
    print("Total questions:", total_questions)
    print("Correct answers:", percentage, "%")

    if percentage >= 80:
        print("Excellent! You did a great job!")
    elif percentage >= 50:
        print("Good job! Keep practising!")
    else:
        print("You need more practice. Try again!")