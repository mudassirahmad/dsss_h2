import random


def get_operand(min, max):
    """
    Generate a random integer between min_val and max_val (inclusive).

    Parameters:
    - min_val (int): The minimum value for the random integer.
    - max_val (int): The maximum value for the random integer.

    Returns:
    int: A random integer between min_val and max_val.
    """
    return random.randint(min, max)


def get_operator():
    """
    Get a random mathematical operator (+, -, *).

    Returns:
    str: A randomly selected mathematical operator.
    """

    return random.choice(['+', '-', '*'])


def perform_operation(operand_1, operand_2, operator):
    """
    Perform a mathematical operation on two operands.

    Parameters:
    - operand_1 (int): The first operand.
    - operand_2 (int): The second operand.
    - operator (str): The mathematical operator (+, -, *).

    Returns:
    tuple: A tuple containing the math problem (as a string) and the result of the operation.

    Example:
    >>> perform_operation(3, 4, '+')
    ('3 + 4', 7)
    """

    # Build the math problem string
    problem = f"{operand_1} {operator} {operand_2}"

    # Perform the specified operation
    if operator == '+': answer = operand_1 + operand_2
    elif operator == '-': answer = operand_1 - operand_2
    else: answer = operand_1 * operand_2
    return problem, answer

def math_quiz():
    """
    Run a math quiz game.

    The user is presented with math problems and needs to provide correct answers.
    Prints the final score at the end.
    """

    score = 0

    # Determine the total number of problems for the quiz
    total_problems = get_operand(2,5)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_problems):
        operand_1 = get_operand(1, 10); operand_2 = get_operand(1, 5); operator = get_operator()

        # Generate a math problem and correct answer
        problem, correct_answer = perform_operation(operand_1, operand_2, operator)
        print(f"\nQuestion: {problem}")

        # Get user input for the answer, handle non-integer input
        while True:
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)
                break  # Exit the loop if conversion to int succeeds
            except ValueError:
                print("Invalid input! Please enter a valid integer.\n")

        user_answer = int(user_answer)

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_problems}")

if __name__ == "__main__":
    math_quiz()
