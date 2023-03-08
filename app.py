from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# a list to store the todo items
todo_items = []

@app.route('/')
def index():
    return render_template('index.html', todo_items=todo_items)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_item = request.form['todo_item']
    todo_items.append(todo_item)
    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_todo(index):
    todo_items.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
