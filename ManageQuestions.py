import random


def manage_questions(questions: list, number_questions: int) -> list:
    # random.sample elige preguntas distintas y nunca se queda en un bucle infinito
    number_questions = min(number_questions, len(questions))
    return random.sample(questions, number_questions)


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
