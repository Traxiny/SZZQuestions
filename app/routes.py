from app import app, render_template, szz_questions
from flask import jsonify, request

@app.route('/', methods=['GET','POST'])
def index():   
    return render_template('index.html')

@app.route("/get/random/questionToLearn")
def get_random_question_to_learn():
    if szz_questions.questions_dict:
        question = szz_questions.get_random_question()
        app.last_question_number = question.question_number
        return {'question' :  f"{question.question_number}. " + question.topic, 'ask_freq': f"Asked {question.question_frequency} times"}
    else:
        return {'question' : None}

@app.route("/get/random/questionToAnswer")
def get_random_question_to_answer():
    if szz_questions.questions_dict:
        question = szz_questions.get_random_question()
        subtopic = question.get_random_subtopic()
        print(subtopic)
        app.last_question_number = question.question_number
        app.last_subtopic_name = subtopic
        return {'question' :  f"{question.question_number}. " + question.topic, 'subtopic': f"{subtopic}"}
    else:
        return {'question' : None}

@app.route('/get/question/subtopics', methods=['GET'])
def get_question_subtopics():
    if hasattr(app, 'last_question_number'):
        question = szz_questions.questions_dict[app.last_question_number]
        subtopic_names = list(question.subtopics.keys())
        return jsonify({'subtopics': subtopic_names})
    else:
        return jsonify({'subtopics': None})

@app.route('/get/question/subtopicHelpers', methods=['GET'])
def get_question_subtopic_specific_helpers():
    subtopic_name = request.args.get('subtopic')
    if hasattr(app, 'last_question_number'):
        question = szz_questions.questions_dict[app.last_question_number]
        helpers = question.subtopics[subtopic_name]
        return jsonify({'helpers': helpers})
    else:
        return jsonify({'helpers': None})

@app.route('/get/question/helpers', methods=['GET'])
def get_question_subtopic_helpers():
    if hasattr(app, 'last_subtopic_name') and hasattr(app, 'last_question_number'):
        question = szz_questions.questions_dict[app.last_question_number]
        helpers = question.get_subtopic_helpers_by_subtopic_name(app.last_subtopic_name)
        return jsonify({'helpers': helpers})
    else:
        return jsonify({'helpers': None})