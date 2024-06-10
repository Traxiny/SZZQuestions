from app import app, render_template, szz_questions
from flask import jsonify

@app.route('/', methods=['GET','POST'])
def index():   
    return render_template('index.html')

@app.route("/get/random/question")
def get_random_question():
    if szz_questions.questions_dict:
        question = szz_questions.get_random_question()
        app.last_question_number = question.question_number
        return {'question' :  f"{question.question_number}. " + question.question_name, 'ask_freq': f"Asked {question.question_frequency} times"}
    else:
        return {'question' : None}

@app.route('/get/question/helpers', methods=['GET'])
def get_question_helpers():
    if hasattr(app, 'last_question_number'):
        question = szz_questions.questions_dict[app.last_question_number]
        return jsonify({'helpers': question.question_helpers})
    else:
        return jsonify({'helpers': None})
    