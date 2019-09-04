from package import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/index')
def change():
    return "goodbye world!"

@app.route('/test')
def test():
    return "testtesttest"
