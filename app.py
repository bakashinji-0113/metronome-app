from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')  # templates/index.html を呼び出す

if __name__ == "__main__":
    app.run(debug=True)