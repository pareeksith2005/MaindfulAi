def remove_duplicates(applications):
    unique_apps = []
    seen_emails = set()

    for app in applications:
        if app.email not in seen_emails:
            unique_apps.append(app)
            seen_emails.add(app.email)

    return unique_apps
