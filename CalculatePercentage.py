def calculate_percentage(score: int, total_questions: int) -> float:
    if total_questions == 0:
        return 0.0
    return (score / total_questions) * 100