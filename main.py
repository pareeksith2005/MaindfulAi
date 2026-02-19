from models import Application
from validator import validate_application
from duplicate_checker import remove_duplicates
from shortlisting_engine import shortlist
from csv_loader import load_applications
applications = load_applications("sample_applications.csv")
valid_apps = [app for app in applications if validate_application(app)]
unique_apps = remove_duplicates(valid_apps)
final_list = shortlist(unique_apps, "Python", threshold=40)
print("\n==============================")
print("   SHORTLISTED CANDIDATES")
print("==============================\n")
if not final_list:
    print("No candidates met the criteria.")
else:
    for index, app in enumerate(final_list, start=1):
        print(f"Candidate {index}")
        print(f"Name       : {app.name}")
        print(f"Email      : {app.email}")
        print(f"Experience : {app.experience} months")
        print(f"Score      : {app.score}")
        print("-" * 30)
