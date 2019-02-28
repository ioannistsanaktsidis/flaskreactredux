from testapp import db
from .serializers import test_schema


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Test %r>' % self.name

    def serialize(self):
        return test_schema.dump(self).data
