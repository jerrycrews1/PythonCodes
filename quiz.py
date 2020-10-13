""" Allows a user to take a quiz.

Classes:
    Question: A single question.
    Quiz: A quiz made of up Question objects.

Functions:
    main: Allows a user to input an answer for each question and checks that answer.

Todo:
    Show the user the questions they got wrong.
    Tell the user how many questions they got right out of how many.
    Add error handling for user input.
"""
import random


class Question:
    """ Represents a single question.

    Attributes:
        question_text (str): The question text.
        options (dict): A list of potential answers
        question_answer (int): The key to the answer to the question.
        correct (bool): A boolean that is true if the question was answered correctly.

    Methods:
        check_answer: Determines whether the answer to the question is correct.
        pretty_print: Prints the question.
    """

    def __init__(self, question_text, options, question_answer):
        """ Initializes a Question object.

        Side Effects:
            Sets attributes question_text, options, question_answer, and correct.
        """
        self.question_text = question_text
        self.question_answer = question_answer
        self.options = options
        self.correct = False

    def pretty_print(self):
        print(f"{self.question_text}:")
        for key, value in self.options.items():
            print(f"{key}: {value}")

    def check_answer(self, answer_key):
        if self.question_answer == answer_key:
            return True
        return False


class Quiz:
    """ A quiz made of up Question objects.

    Attributes:
        questions (list): A list of Question objects.
        answers (list): A list of user answers.
        num_questions (int): The number of questions the user will be asked to answer.
    """

    def __init__(self):
        """ Initializes a Quiz object.

        Side Effects:
            Sets attribute questions and answers to empty lists.
        """
        self.questions = list()
        self.answers = list()

    def print_all_questions(self):
        (question.pretty_print for question in self.questions)

    def add_questions_inline(self, questions):
        """ Adds a list of questions NOT ALREADY INSTATIATED.

        Attributes:
            questions (list): list of questions to add to self.questions. Each item in the list should be a list
                              with a quesiton text, options list, and answer. 
                              Ex: quesitons = [["what is 2+2", {1: 4, 2: 5}, 1], ["What is azul in English?", {1: 'blue', 2: 'green'}, 1]]

        Side Effects:
            Adds the Question objects to self.questions.
        """
        (self.questions.append(
            Question(question[0], question[1], question[2])) for question in questions)

    def add_question_objects(self, questions):
        """ Adds a list of Question objets that are already instantiated to the quiz.

        Arguments:
            questions (list): list of Question objects.

        Side Effects:
            Adds the Question objects to self.questions.
        """

    def read_questions_from_file(self, filename):
        """ Reads questions in from a file.

        Arguments:
            filename (str): The name of the file containing the questions.
                            This file should start with the question_text,
                            and then have the correct answer, and then the options after.
                            example: 
                            What is Michael Scott's middle name?| 1| Gary| Jim| Phillip| Turnip
                            What county in Pennsylvania is Dunder Mifflin Scranton branch located?| 4| Mitchell| Utica| Scranton| Lakawanna

        Side Effects:
            Adds Question objects to questions attribute.

        """
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                values = line.strip().split('|')
                options = {ind + 1: value for ind,
                           value in enumerate(values[2:])}
                self.questions.append(
                    Question(values[0], options, int(values[1])))

    def grade_quiz(self, questions_asked, answers):
        """ Grades a quiz object.

        Arguments:
            answers (list): User's answers that are also the keys to the Question.options attribute.
            questions_asked (list): List of the Question objects the user was asked.

        Returns:
            score (float): Score of the user's quiz.  Number of correct answers / Total and changed to a percentage.

        Side Effects:
            Changes the question object's correct attribute to true if the answer is correct.
        """
        correct = 0
        for ind, question in enumerate(questions_asked):
            if question.check_answer(answers[ind]):
                correct += 1
                question.correct = True
        return (correct / len(questions_asked)) * 100


def main():
    """ Allows a user to take a quiz.

    Creates a Quiz object, reads in questions from a file, and asks a user
    for their answers.

    Returns:
        (float): The score the user got on the quiz.
    """

    quiz = Quiz()
    quiz.read_questions_from_file('questions.txt')
    num_questions = int(input(
        f"How many questions would you like to answer? There are {len(quiz.questions)} questions in this quiz. > "))
    answers = []
    questions_to_ask = random.sample(quiz.questions, num_questions)
    for question in questions_to_ask:
        question.pretty_print()
        answer_to_current_question = int(input(
            "Enter the number corresponding to the correct answer: "))
        answers.append(answer_to_current_question)
    return quiz.grade_quiz(questions_to_ask, answers)


if __name__ == "__main__":
    score = main()
    print(f"Your score is: {round(score, 2)}%")
