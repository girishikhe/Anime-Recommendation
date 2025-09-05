import os
from pathlib import Path 

project_name = "ANIME RECOMMENDER"

list_of_files = [
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/data_loader.py",
    f"{project_name}/src/promp_template.py",
    f"{project_name}/src/recommender.py",
    f"{project_name}/src/vector_store.py",
    f"{project_name}/app/__init__.py",
    f"{project_name}/app/app.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/config.py",
    f"{project_name}/data",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/pipeline.py",
    f"{project_name}/ppieline/build_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/custom_exceptions.py",
    f"{project_name}/utils/logger.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    ".gitignore",
    "README.md",

    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")