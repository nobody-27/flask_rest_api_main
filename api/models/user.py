from ..utils import db

class User(db.Model):
    __table__name__='users'
    id = db.Column(db.Interger(),primary_key=True)
    username=db.Column(db.String(45),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password_hash = db.Column(db.Text(),nullable=False)
    is_staff = db.Column(db.Boolean(),default=False)
    is_active = db.Column(db.Boolean(),default=False)
    orders = db.relationship('Order',backred='customer',lazy=True)

    def __repr__(self):
        return f"<User {self.username}"