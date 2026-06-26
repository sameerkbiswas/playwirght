import subprocess
from tabnanny import check
features_files=[
   "register.feature",
   "yahoo.feature",
   "gmail.feature"
]
for feature in features_files:
    print(f"Running feature: {feature}")
    subprocess.run(["behave", feature], check=True)