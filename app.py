from django.shortcuts import render
from flask import Flask, render_template, request
import random, copy

# initializing the flask app
app = Flask(__name__)

questions = {
    # Format:  'question':[option1, option2, option3, option4, answer_idx]
    'What is the size of int datatype in C/C++ ?':['2','1','4','8'],
    'Which of the following searching techniques do not require the data to be in sorted form ?':['Linear Search','Interpolation Search','Binary Search','All of the above'],
    'How many swaps are required to sort the given array using bubble sort - { 2, 5, 1, 3, 4} ?':['4','5','6','7'],
    'Program with highest run-time complexity is':['Fibonacci Series','Tower of Hanoi','Prime Number Series', 'None of the above']
}
# Format: 'question':'answer'
answers = {'What is the size of int datatype in C/C++ ?':'4','Which of the following searching techniques do not require the data to be in sorted form ?':'Binary Search',
           'How many swaps are required to sort the given array using bubble sort - { 2, 5, 1, 3, 4} ?' :'4','Program with highest run-time complexity is':'Tower of Hanoi'}
# to improve the storage and processing further, a sqlite database can be linked to the flask app

@app.route('/')
def quiz():
    return render_template('homepage.html')

@app.route('/main.html')
def takequiz():
    return render_template('main.html', o = questions)

# this function calculates the number of correct answers/score by using request.form function
@app.route('/quiz', methods=['POST'])
def quiz_answers():
    correct = 0
    for question in questions.keys():
        answered = request.form[question]
        if answers[question] == answered:
            correct = correct+1
    return render_template('result.html',res = correct)


if __name__ == '__main__':
 app.run(debug=True)