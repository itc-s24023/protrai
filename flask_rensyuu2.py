# s24023
# flask_rensyuu2.py
# こんにちはは世界と書かれたHTML文章を表示するプログラムを書く



from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0' ,port=6423)
