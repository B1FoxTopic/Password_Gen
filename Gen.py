from flask import Flask, request, render_template
import random
import string
import hashlib

app = Flask(__name__)

def generate_password(min_length=10, max_length=16, blacklist=None):
    if blacklist is None:
        blacklist = "{,},],[,~,|,(,),`,;,:,.,<,>,\,/"
    length = random.randint(min_length, max_length)
    characters = "".join(c for c in string.ascii_letters + string.digits + string.punctuation if c not in blacklist)
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = generate_password()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if request.method == 'POST':
        blacklist = request.form.get('blacklist')
        password = generate_password(blacklist=blacklist)
        password_hash = hashlib.sha256(password.encode()).hexdigest()
    return render_template('index.html', password=password, password_hash=password_hash)

if __name__ == '__main__':
    app.run()
