from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('test.html')  # Remove the absolute path
#def index():
    # Get the absolute path of the directory containing this script
if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=8000)