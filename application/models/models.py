from application import db
import datetime

# class Sample(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     image_url = db.Column(db.String)
#     text = db.Column(db.String, nullable=False)
#     target_id = db.Column(db.Integer, db.ForeignKey('target.id'))
#     target = db.relationship('Target', backref=db.backref('recommendation', lazy='dynamic'))
#     upvotes = db.Column(db.Integer)
#
#     def __init__(self, text, target, image_url='', upvotes=0, ):
#         self.text = text
#         self.target = target
#         self.upvotes = upvotes
#         self.image_url = image_url
#         self.created_at = datetime.datetime.now()