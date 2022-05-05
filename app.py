from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline
model = pipeline("sentiment-analysis")
import webbrowser

app = Flask(__name__)
webbrowser.open_new("http://127.0.0.1:5000/sentiment_analysis")

@app.route("/sentiment_analysis", methods=['GET', 'POST'])
def sentiment_analysis():
    
    review = ""
    sentiment = ""
    
    if request.method == "POST":
        review = request.form.get("Sentiment")
        result = model(review)
        # output is label and score
        sentiment = result[0]['label']
        
        redirect(url_for("sentiment_analysis"))
    
    return render_template("home.html", review=review, sentiment=sentiment)

if __name__ == "__main__":
    app.run()
    
