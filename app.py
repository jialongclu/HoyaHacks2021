from flask import Flask, render_template, request
from SearchForm import SearchForm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/displayTweets', methods=['GET', 'POST'])
def displayTweets():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        twitterUser = form.username.data
        companyName = form.company.data
        return 'It was validated'
    return 'Wrong'
if __name__ == '__main__':
    app.run(debug=True)