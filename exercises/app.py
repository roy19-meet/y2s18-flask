from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
  players = ["cr7","pva10","da9"] 
  return render_template("first_webpage.html",players=players,likes_same_sport=True)

if __name__ == '__main__':
   app.run(debug = True)