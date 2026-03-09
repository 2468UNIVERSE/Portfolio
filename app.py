from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # render_template looks for an html file in the 
    # "templates" folder.
    # it sends the content of index.html to the user's browser
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)