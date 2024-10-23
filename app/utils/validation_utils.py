from marshmallow import Schema, fields, validate, ValidationError

class UserRegistrationSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))
    phone = fields.String(validate=validate.Length(min=10, max=15))
    role = fields.String(required=True, validate=validate.OneOf(["Administrador", "Supervisora", "Vendedora"]))

class RouteSchema(Schema):
    route_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    creation_date = fields.DateTime(required=True)
    id_administrator = fields.Integer(required=True)
