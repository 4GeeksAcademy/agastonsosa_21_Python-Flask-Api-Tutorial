from flask import Flask, jsonify, request
app = Flask(__name__)

todos=[ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    print("Updated todos list:", todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    POSITIVE= position >= 0
    LESS_THAN_MAXLENGTH= position < len(todos)
    if POSITIVE and LESS_THAN_MAXLENGTH:
        deleted_todo = todos.pop(position)
        print("You have deleted task:", deleted_todo)
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid position"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
