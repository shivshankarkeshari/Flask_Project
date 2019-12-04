from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
#two route handle by same function
@app.route('/home')
def hello_world():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__=="__main__":
	app.run(debug=True)

# app.config['DEBUG'] = True
