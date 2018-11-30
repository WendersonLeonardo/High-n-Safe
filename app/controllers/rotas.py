from app import app

@app.route("/")
def index():
    return("Pagina Principal")