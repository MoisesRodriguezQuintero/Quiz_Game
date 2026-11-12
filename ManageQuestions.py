import random


def manage_questions(questions:str, number_questions:int):
    selected_questions = []
    while len(selected_questions) < number_questions:
        question = random.choice(questions)

        if question not in selected_questions:
            selected_questions.append(question)
    return selected_questions

questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Madrid", "Paris", "Rome", "London"],
        "correct": 2
    },
    {
        "question": "How many days are there in a week?",
        "answers": ["Five", "Six", "Seven", "Eight"],
        "correct": 3
    },
    {
        "question": "What is 5 x 5?",
        "answers": ["10", "15", "20", "25"],
        "correct": 4
    }
]