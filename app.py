
from flask import Flask, redirect, render_template, request, url_for
import flask
import yfinance as yf



app = Flask(__name__)
@app.route("/", methods = ["POST", "GET"])
def home():
        if request.method == "POST":
                stockPrediction = request.form["symbol"]
                return redirect(url_for("stockPrediction", sock=stockPrediction))
        else:
                return render_template("index.html")

@app.route("/<sock>")
def stockPrediction(sock):
        try:
                while True:
                        ticker = yf.Ticker(sock)
                        pe, eps = ticker.info['trailingPE'], ticker.info['trailingEps']
                        price = eps * pe

                        price = "The estimated price is " + str(round(price, 2))

                        return render_template("stonk.html", price = price)
        except KeyError:
                return "<h1>An Error Has Occured Please Remember to Put The Stock Symbol and NOT the Company's name. Thank You</h1>"

        

if __name__ == '__main__':
    app.run()