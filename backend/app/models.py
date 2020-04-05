from . import db

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(100))
    from_where = db.Column(db.String(200),default="none")
    msg = db.Column(db.String(400))

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(400))
    logo = db.Column(db.String(400))
    date = db.Column(db.String(100))

