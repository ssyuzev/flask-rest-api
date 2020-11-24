import marshmallow


class HealthcheckSchema(marshmallow.Schema):
    status = marshmallow.fields.Str()
