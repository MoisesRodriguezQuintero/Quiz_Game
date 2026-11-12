def show_question(question: str, options: list[str]) -> None:
    """
    Show's a question to the user with given options.

    Args:
        question (str): Text of the question to show.
        options (list of str): List of options to show.

    Returns:
        None
    """
    print(question)

    print("Choose an option:")
    for index, option in enumerate(options):
        print(index, option)