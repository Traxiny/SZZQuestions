import re
import random
import json

class SZZQuestions:
    def __init__(self):
        self.questions_dict = {}
        self.questions_count = 0
        self.__read_raw_file()

    def get_question(self, number):
        return self.questions_dict.get(number)
    
    def get_random_question(self): # maybe add frequency
        return self.questions_dict.get(random.randint(1,self.questions_count))
    
    def get_questions_by_frequency(self, freq: int) -> list[str]:
        return [
            f"{question.question_number}.{question.topic} - {question.question_frequency}"
            for question in self.questions_dict.values()
            if question.question_frequency == freq
        ]

    def get_questions_greater_than_or_equal_frequency(self, freq: int) -> list[str]:
        return [
            f"{question.question_number}.{question.topic} - {question.question_frequency}"
            for question in self.questions_dict.values()
            if question.question_frequency >= freq
        ]

    def get_questions_less_than_or_equal_frequency(self, freq: int) -> list[str]:
        return [
            f"{question.question_number}.{question.topic} - {question.question_frequency}"
            for question in self.questions_dict.values()
            if question.question_frequency <= freq
        ]
    
    def __read_raw_file(self):
        with open("Questions.json", "r") as f:
            questions = json.load(f)

        for question in questions:
            question_info = question['question']
            question_number = question_info['number']
            self.questions_dict[question_number] = Question(
                number=question_number,
                topic=question_info['topic'],
                subtopics=question_info['subtopics'],
                frequency=0
            )
            self.questions_count += 1
    
    def __repr__(self):
        return f"SZZQuestions(questions_dict={self.questions_dict})"
    
class Question:
    def __init__(self, number, topic, frequency, subtopics):
        self.topic = topic
        self.question_number = number
        self.subtopics = {subtopic['name']: subtopic['helpers'] for subtopic in subtopics}
        self.question_frequency = frequency

    def get_random_subtopic(self):
        print(self.subtopics)
        random_subtopic_name = random.choice(list(self.subtopics.keys()))
        return random_subtopic_name
    
    def get_subtopic_helpers_by_subtopic_name(self, subtopic_name):
        return self.subtopics.get(subtopic_name)
    
    def __repr__(self):
        subtopics_repr = ', '.join(f"{name}: {helpers}" for name, helpers in self.subtopics.items())
        return f"Question(number={self.question_number}, name={self.topic!r}, frequency={self.question_frequency!r}, subtopics={{ {subtopics_repr} }})"