def calculate_score(app, required_skill):
    score = 0

    if required_skill.lower() in [s.lower() for s in app.skills]:
        score += 50

    score += 5 * (len(app.skills) - 1)

    if app.availability.lower() == "full-time":
        score += 20

    if app.experience >= 6:
        score += 20

    return score


def shortlist(applications, required_skill, threshold=30):
    shortlisted = []

    for app in applications:
        app.score = calculate_score(app, required_skill)
        if app.score >= threshold:
            shortlisted.append(app)

    shortlisted.sort(key=lambda x: x.score, reverse=True)

    return shortlisted
