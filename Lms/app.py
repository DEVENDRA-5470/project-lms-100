from flask import *
from models import *
from flask_migrate import *
from sqlalchemy import text
from config import Config
from db import *
from routes.students_routes import student_bp
from routes.authors_routes import author_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/db-health")
def db_health():
    try:
        db.session.execute(text("SELECT 1"))
        return {"status":"ok","database":"Connected"}
    except Exception as e:
        return {"status":str(e)}

@app.route("/")
def home():
    return render_template("home.html")

app.register_blueprint(student_bp, url_prefix="/student")
app.register_blueprint(author_bp, url_prefix="/author")

if __name__ == "__main__":
    app.run(debug=True)