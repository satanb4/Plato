import requests

base_url =" https://opentdb.com/api.php?amount=10&category=17&type=multiple"


def print_top_level_collections():
    url = base_url
    r = requests.get(url)
    collections = r.json()
    with open('question.json', 'w') as outfile:  
        json.dump(collections, outfile)
    q=[]
    a=[]
    for i in collections['results']:
        q.append(i['question'])
        temp=[]
        temp.append(i['correct_answer'])
        k=i['incorrect_answers']
        a.append(temp+k)    
    d={'questions':q,'answers':a}
    return d

print(print_top_level_collections())