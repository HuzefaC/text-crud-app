from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['word']
        new_word = Word(word=word)
        try:
            db.session.add(new_word)
            db.session.commit()
            return redirect('/')
        except:
            return "Error in adding the word"
    else:
        words = Word.query.all()
        return render_template('index.html', words=words, len=len(words))


if __name__ == "__main__":
    app.run(debug=True)
