def show_question(question: str, options: list[str]) -> None:
    """
    Shows a question to the user with the given options.

    Args:
        question (str): Text of the question to show.
        options (list of str): List of options to show.

    Returns:
        None
    """
    print("\n" + question)

    print("Choose an option:")
    # Empezamos en 1 para que coincida con el campo "correct"
    for index, option in enumerate(options, start=1):
        print(index, option)
