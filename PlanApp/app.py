from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['input']
    # For now, simply echo back the user's input
    response = {'text': user_input}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
