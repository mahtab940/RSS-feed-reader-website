from flask import Flask, request, render_template
import feedparser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    items = []
    url = ''

    if request.method == 'POST':
        url = request.form['rss_url']
        feed = feedparser.parse(url)

        if feed.bozo:
            items = [{'title': 'Invalid RSS Feed', 'link': '#', 'summary': 'Could not parse the feed.'}]
        else:
            items = feed.entries[:10]

    return render_template('index.html', items=items, url=url)

if __name__ == '__main__':
    app.run(debug=True)
