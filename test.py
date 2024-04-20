from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')  # Remove the absolute path
#def index():
    # Get the absolute path of the directory containing this script
if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=8000)
