import uuid
from enum import Enum
from swarm_intelligence_app.models import db


class InvitationStatus(Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    CANCELLED = 'cancelled'


class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(36), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Enum(InvitationStatus), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'),
                                nullable=False)

    def __init__(self, email, organization_id):
        self.code = str(uuid.uuid4())
        self.email = email
        self.status = InvitationStatus.PENDING
        self.organization_id = organization_id

    def __repr__(self):
        return '<Invitation %r>' % self.id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'email': self.email,
            'status': self.status.value,
            'organization_id': self.organization_id
        }