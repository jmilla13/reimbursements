import os
from flask import Flask, url_for, render_template, request, flash
from form import ContactForm



app = Flask(__name__)

app.secret_key = 'development key'

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reimbursements', methods=['GET', 'POST'])
def submission():
  form = ContactForm()
 
  if request.method == 'POST':
    return render_template('request.html', success=True)
 
  elif request.method == 'GET':
    return render_template('request.html', form=form)


if __name__ == "__main__":
    app.run(debug = True)