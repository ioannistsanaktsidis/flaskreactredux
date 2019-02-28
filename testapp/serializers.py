from marshmallow import Schema, fields


class TestSchema(Schema):
    key = fields.Str()
    value = fields.Str()


test_schema = TestSchema()
