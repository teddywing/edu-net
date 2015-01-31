from modules.shared.models import db


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False, unique=True)

    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())


class UserInterest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'),
        primary_key=True)

    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
