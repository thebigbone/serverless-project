from flask import Flask, request, render_template, render_template_string
import requests

app = Flask(__name__)


def site(text, specific_words):
    url = f'https://test938103.azurewebsites.net/api/httptrigger1/?text={text}&specific_words={specific_words}'
    response = requests.get(url).text

    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/trigger', methods=["GET"])
def trigger():
    text = request.args.get('text')
    specific_words = request.args.get('specific_words')

    response_site = site(text, specific_words)
    return render_template('trigger.html', response=response_site, text=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)
