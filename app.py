from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])#desnecessário, já que o get é método padrão
def home():
    return "It's running as a charm", 200

if __name__ == '__main__':
    app.run(debug=True)