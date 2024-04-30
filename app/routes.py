from flask import render_template, request, redirect, url_for

def configure_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add', methods=['GET', 'POST'])
    def add():
        if request.method == 'POST':
            num1 = request.form['num1']
            num2 = request.form['num2']
            result = float(num1) + float(num2)
            # Database insertion logic would be handled here
            return render_template('add.html', result=result)
        return render_template('add.html', result=None)
