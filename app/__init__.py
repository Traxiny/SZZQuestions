from flask import Flask, render_template
from SZZQuestions import SZZQuestions

app = Flask(__name__)

szz_questions = SZZQuestions()
last_question_number = 0
last_subtopic_name = ""

from app import routes