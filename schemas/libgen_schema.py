from marshmallow import Schema, fields


class LibgenRowSchema(Schema):
    _id = fields.Integer(required=True)
    authors = fields.String(required=True)
    title = fields.String(required=True)
    publisher = fields.String(required=False)
    year = fields.Integer(required=False)
    pages = fields.Integer(required=False)
    language = fields.String(required=True)
    size = fields.String(required=True)
    extension = fields.String(required=True)
    mirror_1 = fields.Url(required=False)
    mirror_2 = fields.Url(required=False)
    mirror_3 = fields.Url(required=False)
    mirror_4 = fields.Url(required=False)
    mirror_5 = fields.Url(required=False)
    edit = fields.Url(required=False)
