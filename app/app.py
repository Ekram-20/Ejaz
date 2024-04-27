from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/summarize-youtube')
def summarize_video(url): 
    return render_template('index.html')

@app.route('/summarize-sound')
def summarize_sound(sound): 
    return render_template('index.html')





if __name__ == '__main__': 
    app.run(debug=True)