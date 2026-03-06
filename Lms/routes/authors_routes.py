from flask import *
author_bp=Blueprint("author",__name__)

@author_bp.route("/author-register")
def author_register():
    return render_template("author/author-register.html")

@author_bp.route("/author-login")
def author_login():
    return "Login here for authors."