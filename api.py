from logging import error
from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact': '018273956',
        'name': 'bob'
    },
    {
        'id': 2,
        'contact': '619373928',
        'name': 'sarah'
    },
    {
        'id': 3,
        'contact': '019279392',
        'name': 'james'
    },

]


@app.route('/Hi')
def displayHello():
    return 'Cookie likes to eat cookies'


@app.route('/tasks', methods=['POST'])
def writing():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Please give task to be added! :)'

        })
    task = {
        'id': tasks[-1]['id']+1,
        'contact': request.json['contact'],
        'name': request.json['name']
    }
    tasks.append(task)
    return jsonify({
        'status': 'Success',
        'message': 'Task Added Successfully! :D'
    })

@app.route('/showtasks')
def display():
    return jsonify({
        'data':tasks
    })




if (__name__ == '__main__'):
    app.run(debug=True)
