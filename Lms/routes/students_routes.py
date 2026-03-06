from flask import *
student_bp=Blueprint("student",__name__)

@student_bp.route("/student-register",methods=["POST","GET"])
def student_register():
    if request.method=="POST":
        full_name=request.form.get("full_name")
        return full_name
        
    else:
        return render_template("students/register-student.html")


@student_bp.route("/student-login")
def student_login():
    return "Login here for students."