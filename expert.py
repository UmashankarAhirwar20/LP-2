def main():
    print("Welcome to the Stock Market Trading System!")
    print("Please answer the following questions:")

    trend = ask_question("What is the current market trend? (Upwards/Downwards): ", ["upwards", "downwards"])
    fundamentals = ask_question("How are the fundamentals of the company? (strong/weak): ", ["strong", "weak"])
    indicators = ask_question("What do the technical indicators suggest? (positive/negative): ", ["positive", "negative"])

    should_buy = evaluate(trend, fundamentals, indicators)

    print_result(should_buy)

def ask_question(question, valid_responses):
    """
    Ask a question to the user and validate the input.

    Parameters:
        question (str): The question to ask the user.
        valid_responses (list): A list of valid responses.

    Returns:
        str: The user's response, validated against the list of valid responses.
    """
    while True:
        response = input(question).strip().lower()
        if response in valid_responses:
            return response
        print(f"Invalid input. Please provide one of the following: {', '.join(valid_responses)}")

def evaluate(trend, fundamentals, indicators):
    """
    Evaluate the trading decision based on the user's inputs.

    Parameters:
        trend (str): The market trend.
        fundamentals (str): The company's fundamentals.
        indicators (str): The technical indicators' suggestions.

    Returns:
        bool: True if the recommendation is to buy the stock, False otherwise.
    """
    return trend == "upwards" and fundamentals == "strong" and indicators == "positive"

def print_result(should_buy):
    """
    Print the result of the trading decision.

    Parameters:
        should_buy (bool): True if the recommendation is to buy the stock, False otherwise.
    """
    if should_buy:
        print("Recommendation: Buy the stock!")
    else:
        print("Recommendation: Do not buy the stock.")

if __name__ == "__main__":
    main()
