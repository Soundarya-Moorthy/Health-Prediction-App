
from flask import Flask, render_template, request, redirect, url_for
from models import db, Patient
from datetime import datetime
from services.ai_services import predict_health

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///health.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()


# ==========================
# Home Page (Read)
# ==========================
@app.route("/")
def index():

    search = request.args.get("search", "").strip()

    risk = request.args.get("risk", "")

    query = Patient.query

    # Search by Name or Email
    if search:
        query = query.filter(
            (Patient.fullname.ilike(f"%{search}%")) |
            (Patient.email.ilike(f"%{search}%"))
        )

    # Filter by Risk Level
    if risk:
        query = query.filter(Patient.risk_level == risk)

    patients = query.all()

    return render_template(
        "index.html",
        patients=patients,
        search=search,
        risk=risk
    )

# ==========================
# Add Patient (Create)
# ==========================
@app.route("/add", methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":

        # Get AI Prediction
        prediction = predict_health(
            request.form["glucose"],
            request.form["haemoglobin"],
            request.form["cholesterol"]
        )

        # Create Patient
        patient = Patient(
            fullname=request.form["fullname"],
            dob=datetime.strptime(
                request.form["dob"],
                "%Y-%m-%d"
            ).date(),
            email=request.form["email"],
            glucose=float(request.form["glucose"]),
            haemoglobin=float(request.form["haemoglobin"]),
            cholesterol=float(request.form["cholesterol"]),
            condition=prediction["condition"],
            risk_level=prediction["risk_level"],
            recommendation=prediction["recommendation"]
        )

        db.session.add(patient)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_patient.html")

# ==========================
# Edit Patient (Update)
# ==========================
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_patient(id):

    patient = Patient.query.get_or_404(id)

    if request.method == "POST":

        patient.fullname = request.form["fullname"]

        patient.dob = datetime.strptime(
            request.form["dob"],
            "%Y-%m-%d"
        ).date()

        patient.email = request.form["email"]

        patient.glucose = float(request.form["glucose"])

        patient.haemoglobin = float(request.form["haemoglobin"])

        patient.cholesterol = float(request.form["cholesterol"])

        # Generate New AI Prediction
        prediction = predict_health(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        patient.condition = prediction["condition"]
        patient.risk_level = prediction["risk_level"]
        patient.recommendation = prediction["recommendation"]

        db.session.commit()

        return redirect(url_for("index"))

    return render_template("edit_patient.html", patient=patient)

# ==========================
# Delete Patient
# ==========================
@app.route("/delete/<int:id>")
def delete_patient(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)