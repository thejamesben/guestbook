from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for simplicity
entries = []

@app.route('/', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('comment')
        entries.append({'name': name, 'comment': comment})
        return redirect(url_for('guestbook'))
    return render_template('guestbook.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
