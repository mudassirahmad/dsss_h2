import unittest
from math_quiz import get_operand, get_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_get_operand(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_operand(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_operator(self):
        # Test if the returned operator is one of the specified operators
        operators = set(['+', '-', '*'])
        for _ in range(1000):  # Test a large number of random values
            operator = get_operator()
            self.assertIn(operator, operators)

    def test_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 4, '*', '3 * 4', 12),
                (10, 5, '-', '10 - 5', 5),
                (5, 10, '-', '5 - 10', -5)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Test if the generated problem and answer match the expected values
                problem, answer = perform_operation(num1, num2, operator)

                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
