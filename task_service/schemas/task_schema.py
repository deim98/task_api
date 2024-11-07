from marshmallow import Schema, fields, ValidationError

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    completed = fields.Bool(required=False, missing=False)  # Default to False if not provided

# Instance of the schema for validation
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
