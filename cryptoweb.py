from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)


key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    action = None

    if request.method == 'POST':
        action = request.form.get('action')
        text = request.form.get('text')

        if action == 'Encrypt':
            encrypted_text = cipher_suite.encrypt(text.encode()).decode()
            result = encrypted_text
        elif action == 'Decrypt':
            try:
                decrypted_text = cipher_suite.decrypt(text.encode()).decode()
                result = decrypted_text
            except Exception:
                result = 'Decryption failed. Invalid input.'

    return render_template('index.html', result=result, action=action)

if __name__ == '__main__':
    app.run(debug=True)