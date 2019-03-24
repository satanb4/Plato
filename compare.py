import json


def correct_answers(question_file,answer_file):
    correct=0;    
    json1_file = open(question_file)
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    json2_file = open(answer_file)
    json2_str = json2_file.read()
    json2_ans = json.loads(json2_str)
    for i in json1_data['results']:
        for j in json2_ans['results']:
            if i['correct_answer']==j['correct_answer']:
                correct+=1
    return correct


print(correct_answers('question.json','answers.json'))
