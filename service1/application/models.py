from application import db

class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scene = db.Column(db.String(255), nullable=False)
    story = db.Column(db.String(255), nullable=False)