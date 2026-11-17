def update_score(score: int, result: bool) -> int:
    """
    Adds one point to the score if the answer was correct.

    Args:
        score (int): Current score.
        result (bool): Whether the answer was correct.

    Returns:
        int: The updated score.
    """
    if result:
        return score + 1
    return score
