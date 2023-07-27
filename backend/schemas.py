from marshmallow import Schema, fields, validate


class SumNumbersSchema(Schema):
    numbers = fields.List(
        fields.Number(), required=True, validate=validate.Length(min=1)
    )


class ConcatenateStringsSchema(Schema):
    string1 = fields.Str(required=True, validate=validate.Length(max=100))
    string2 = fields.Str(required=True, validate=validate.Length(max=100))
