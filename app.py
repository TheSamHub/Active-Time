from flask import Flask, request, render_template,jsonify
import pickle
import numpy as np
import pandas as pd
import json
'''from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('dataset.csv')
X = dataset['Sleep'].values.reshape(-1,1)
y = dataset['Active'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm

import pickle
filename = 'model.pkl'
pickle.dump(regressor, open(filename, 'wb'))'''

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

def do_something(Your_name,Hours_you_slept):
   Your_name = Your_name.upper()
   Hours_you_slept = Hours_you_slept.upper()
   #combine = Your_name + Hours_you_slept
   arr = np.array([Hours_you_slept]).reshape(-1,1)
   combine = model.predict(arr)
   return combine
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/success', methods =["GET", "POST"])
def successfull():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       your_name = request.form.get("name")
       # getting input with name = lname in HTML form 
       hours = request.form.get("hours") 
       combine = do_something(your_name,hours)
       return your_name+' you should slept for '+str(hours)+ ' and you will be active for around '+ str(round(combine[0][0],2))+' hours.'
    return render_template("index.html")

'''@app.route('/join', methods=['GET','POST'])
def my_form_post():
    
    word = request.args.get('name')
    Hours_you_slept = request.args.get('hours')
    combine = do_something(Your_name,Hours_you_slept)
    result = {
        "output": combine
    }
    #result = {str(key): value for key, value in result.items()}
    #print(result)
    result = pd.Series(combine[0]).to_json(orient='values')
    print(result)
    return f'Output: {result}'''
if __name__ == '__main__':
    app.run(debug=True)