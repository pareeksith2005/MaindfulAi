import csv
from models import Application
def load_applications(file_path):
    applications = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            skills = row["skills"].split("|")
            app = Application(
                row["name"],
                row["email"],
                skills,
                row["role"],
                row["availability"],
                int(row["experience"])
            )
            applications.append(app)

    return applications
