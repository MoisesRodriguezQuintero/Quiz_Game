# Function to check if the player's answer is correct
def check_answer(user_answer: int, correct_answer: int) -> bool:
    """
    Checks if the player's answer is correct.

    Args:
        user_answer (int): The number selected by the player.
        correct_answer (int): The number of the correct option.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """

    # Compare the player's answer with the correct answer
    if user_answer == correct_answer:

        # Return True if both answers are equal
        return True

    else:

        # Return False if the answers are different
        return False