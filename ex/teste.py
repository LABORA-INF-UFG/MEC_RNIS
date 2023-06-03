from flask import Flask, request, jsonify

app = Flask(__name__)
ids = []
next_id = 1

@app.route('/api/id', methods=['POST'])
def generate_id():
    global next_id
    new_id = next_id
    next_id += 1
    ids.append(new_id)
    return jsonify({'id': new_id})

if __name__ == '__main__':
    app.run()