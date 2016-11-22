from swarm_intelligence_app.models import db


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_deleted = db.Column(db.Boolean(), nullable=False)

    partners = db.relationship('Partner', backref='organization')
    invitations = db.relationship('Invitation', backref='organization',
                                  lazy='dynamic')

    def __init__(self, name):
        self.name = name
        self.is_deleted = False

    def __repr__(self):
        return '<Organization %r>' % self.id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_deleted': self.is_deleted
        }
