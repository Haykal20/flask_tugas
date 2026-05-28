from flask import Flask, request, render_template

app = Flask(__name__)

# 1. Home Route (/)
@app.route('/')
def home():
    return render_template('home.html', nama="Haykal Furqan Shafiq", nim="24210076")

# 2. About Route (/about)
@app.route('/about')
def about():
    return render_template('about.html', hobi="Mancing")

# 3. Dynamic Greeting Route (/greet/<name>)
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

# 4. Contact Form Route (/contact)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return render_template('contact.html', submitted=True, name=name, message=message)
    
    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)