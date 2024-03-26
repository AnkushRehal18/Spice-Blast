from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        number = request.form['number']
        time = request.form['time']
        date = request.form['date']

        with open("credentials.txt", "w") as file:
            file.write(f"email = {email} , ")
            file.write(f"number = {number}, ")
            file.write(f"time = {time}, ")
            file.write(f"date = {date}, ")
            file.write(f"\n" )

        flash('You have found the table successfully', category='success')
        return redirect(url_for("index"))

    return render_template('submit.html')


@app.route('/online_order')
def online_order():
    return render_template('online_order.html')


if __name__ == '__main__':
    app.run(debug=True)
