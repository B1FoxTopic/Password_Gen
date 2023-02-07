from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)

def generate_password(min_length=10, max_length=16, blacklist=None):
    if blacklist is None:
        blacklist = "{ , } , ] , [ , ~ , | , ( , ) , ` , ; , :"
    length = random.randint(min_length, max_length)
    characters = "".join(c for c in string.ascii_letters + string.digits + string.punctuation if c not in blacklist)
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = generate_password()
    if request.method == 'POST':
        blacklist = request.form.get('blacklist')
        password = generate_password(blacklist=blacklist)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run()
