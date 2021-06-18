from db import db, ma

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, email, name, created_at, updated_at):
        self.email = email
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get_or_404(id)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "created_at", "updated_at")
        model = User