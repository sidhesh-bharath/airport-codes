from flask import Flask, render_template, request, redirect, url_for
from db import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/")
def index():
    items = AirportInfo.query.all()
    return render_template('index.html', items=items)


@app.route('/add', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        location = request.form['location']

        new_item = AirportInfo(code=code, name=name, location=location)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete_item():
    if request.method == 'POST':
        code = request.form['code']

        item = AirportInfo.query.get(code)
        if item:
            db.session.delete(item)
            db.session.commit()

        return redirect(url_for('index'))

    return render_template('delete.html')


if __name__ == "__main__":
    app.run(debug=True)
