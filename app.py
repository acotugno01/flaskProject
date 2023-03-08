from flask import Flask

app = Flask(__name__)


@app.route('/manager-welcome-page')
def managerWelcomePage():  # put application's code here
    return render_template ('managerWelcomePage.html')

if __name__ == '__main__':
    app.run()
