import re
import random

class SZZQuestions:
    def __init__(self):
        self.questions_dict = {}
        self.questions_count = 0
        self.read_raw_file()

    def get_question(self, number):
        return self.questions_dict.get(number)
    
    def get_random_question(self): # maybe add frequency
        return self.questions_dict.get(random.randint(1,self.questions_count))
    
    def get_questions_by_frequency(self, freq: int) -> list[str]:
        return [
            f"{question.question_number}.{question.question_name}"
            for question in self.questions_dict.values()
            if question.question_frequency == freq
        ]

    def get_questions_greater_than_or_equal_frequency(self, freq: int) -> list[str]:
        return [
            f"{question.question_number}.{question.question_name}"
            for question in self.questions_dict.values()
            if question.question_frequency >= freq
        ]

    def get_questions_less_than_or_equal_frequency(self, freq: int) -> list[str]:
        return [
            f"{question.question_number}.{question.question_name}"
            for question in self.questions_dict.values()
            if question.question_frequency <= freq
        ]
    
    def read_raw_file(self):
        questions_raw = []

        with open("questionsRaw.txt", "r") as f:
            questions_raw = f.read().split("\n\n")
        
        questions = [line.split("\n\t") for line in questions_raw]

        for question in questions:
            if question is None:
                continue

            match = re.match(r'(\d+)\.', question[0])

            if match:
                number = int(match.group(1))
                remains = question[0][match.end():].strip()
                items = [item.strip() for item in remains.split(',')]
                helpers = re.split(r",(?![^()]*\))", question[1])
                self.questions_dict[number] = Question(number, items[0], items[1], helpers)
                self.questions_count += 1
    
    def __repr__(self):
        return f"SZZQuestions(questions_dict={self.questions_dict})"
    
class Question:
    def __init__(self, number, name, frequency, helpers):
        self.question_number = number
        self.question_name = name
        self.question_frequency = frequency
        self.question_helpers = helpers

    def __repr__(self):
        return f"Question(number={self.question_number}, name={self.question_name!r}, frequency={self.question_frequency!r}, helpers={self.question_helpers!r})"