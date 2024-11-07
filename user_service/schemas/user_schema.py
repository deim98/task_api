from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # Only used for serialization
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)

# Instantiate the schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)