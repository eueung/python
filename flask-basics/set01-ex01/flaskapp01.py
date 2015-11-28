from flask import Flask, render_template

app = Flask("app")
app.debug = True

def top_articles():
    return [
        {"title": "Google",
         "link": "http://google.com",
         "date": "just now"
        },
        {"title": "Yahoo",
         "link": "http://yahoo.com",
         "date": "1 minute ago"
        }
   ]

@app.route('/')
def index():
    articles = top_articles()
    return render_template("rows.jinja2.html",
                           rows=articles)

PORT=4001
app.run(host="0.0.0.0", port=PORT, use_reloader=False)