def validate_application(app):
    required_fields = [app.name, app.email, app.skills, app.role]
    return all(required_fields)
