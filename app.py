from flask import Flask,render_template,request,redirect,url_for
import config

app = Flask(__name__)

#@app.route('/')
#def index():
#    return redirect(url_for('/login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
    else:
        return render_template('index.html')

@app.route()

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)

config.cursor.execute("select * from users")
config.rows=cursor.fetchall()
for row in rows:
    print (row)