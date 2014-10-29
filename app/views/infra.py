from app import app

@app.route('/health')
def healthcheck():
    return 'hello world'