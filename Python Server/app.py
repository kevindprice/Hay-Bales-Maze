from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/maze", code=302)

@app.route('/maze')
def maze():
    return render_template('Hay Bales Maze.html')
    
@app.route('/Instructions.html')
def Instructions():
    return render_template('Instructions.html')


#Put "localhost" in the address bar.
if __name__ == "__main__":
    app.run( 
        debug=True,
        host="0.0.0.0",
        port=int("80")
    )  #port 80 is standard HTML