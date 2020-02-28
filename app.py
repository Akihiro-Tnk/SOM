import json
#from flask import Flask
import somalgo
import ast
import random

#app = Flask(__name__)

"""
data = list()
for d in range(100):
    data.append(random.random())
data.append(100)
data = {'numbers': data}
"""

data = {"numbers": [1,1,2,3,4,1,1,4,2,2,1,3,1,3,4,1,4,90,1,21,1,2,3,1,1,2,4,113]}
output = json.dumps(data)
headers = {'Content-type': 'application/json'}


def call_mat():
    try:
        theMagic = somalgo.initialize()
        result = ast.literal_eval(theMagic.somalgo(output))
    except Exception as e:
        print("Exception" + str(e))
    return result['output']


def som():
    result = call_mat()
    anomaly = list()
    for r in result:
        if sum(r) == 1:
            index = r.index(1)
            ano = str(data['numbers'][index])
            anomaly.append(ano)
    """
    indexes = [i for i,x in enumerate(result) if x == 1]
    for i in indexes:
        ano = str(data['numbers'][i])
        anomaly.append(ano)
    """
    return str(anomaly)

print(som())

"""
@app.route('/')
def get():
    req = som()
    return req


if __name__=='__main__':
    app.debug = True
    app.run(debug=True)
"""

