from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/Communication', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        # submission = request.form['Communication']
        # query = "Write a story about a chicken who sells taco: {}".format(submission)
        query = request.form['Communication']
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        # prompt = 'AI Suggestions for {} are:'.format(submission)
        prompt = 'AI Suggestions are:'

    return render_template('communication.html', **locals())

@app.route('/Shopping', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        query = request.form['Shopping']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('shopping.html', **locals())



@app.route('/Computer', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        query = request.form['Computer']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('computer.html', **locals())



@app.route('/Nature', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        query = request.form['Nature']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('nature.html', **locals())


@app.route('/Family', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        query = request.form['Family']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('family.html', **locals())


@app.route('/Travel', methods=["GET", "POST"])
def Travel():    
    if request.method == 'POST':
        print(request.get_json())
        submission = request.form['textprompt']
        text_query = "{}".format(submission)
        query = ''
        prompt = 'AI suggestions are'
        if request.form['submit_button'] == 'Complete' or request.form['submit_button'] == 'Prompt':
          query = text_query          
        if request.form['submit_button'] == 'Verb':
          query = "Tell me five verbs related to travel"
          prompt = 'Verbs you can use are'
        if request.form['submit_button'] == 'Adjective':
          query = "Tell me five adjectives to describe personality"
          prompt = 'Adjectives you can use are'
        print(query)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', ' ')

    return render_template('travel.html', **locals())


@app.route('/Entertainment', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        query = request.form['Entertainment']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('entertainment.html', **locals())


@app.route('/Music', methods=["GET", "POST"])
def videoDescription():

    if request.method == 'POST':
        query = request.form['Music']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('music.html', **locals())

if __name__ == '__main__':
    app.run()
