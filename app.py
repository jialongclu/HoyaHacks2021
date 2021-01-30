from flask import Flask, render_template, request
from SearchForm import SearchForm
from TweetFinder import TweetFinder

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/displayTweets', methods=['GET', 'POST'])
def displayTweets():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        # Handling Twitter
        twitterUser = str(form.username.data)
        companyName = str(form.company.data)
        finder = TweetFinder(twitterUser, companyName)
        filteredTweets = finder.findFilteredTweets()
        user = finder.getUser()
        finder.saveAvatarLocally(user)
        return render_template('displayTweets.html', data=filteredTweets)

    return 'Wrong'
if __name__ == '__main__':
    app.run(debug=True)