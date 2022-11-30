# Conda

## Download and Install Mambaforge ([docs](https://github.com/conda-forge/miniforge#unix-like-platforms))

```
cd ~/Downloads/
curl -L -O "<https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$>(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh

```

1. `[Enter]`
2. `q`
3. `yes`
4. `[Enter]`
5. `yes`

## Setup Blue (Python code formatter)

1. `pip install blue`
2. `which blue` (to get the path)
3. Setup File Watcher:
    - Make sure the [File Watchers](https://plugins.jetbrains.com/plugin/7177-file-watchers) plugin is installed.
    - Preferences → Tools → File Watchers
    - Click the + icon to add a new watcher → <custom>:
        - Name: Blue
        - File type: Python
        - Scope: Project Files
        - Program: <path_from_step_2> (`/Users/elliotwaite/mambaforge/bin/blue`)
        - Arguments: `$FilePath$`
        - Output paths to refresh: `$FilePath$`
        - Working directory: `$ProjectFileDir$`
        - Environemnt variables: [none]
        - Advanced Options:
            - [x]  Auto-save edited files to trigger the watcher
            - [ ]  Trigger the watcher on external changes
            - [ ]  Trigger the watcher regardless of syntax errors
            - [ ]  Create output file from stdout
            - Show console: Never
            - Output filters: [none]

## Setup a PyCharm Project

1. Add an `environment.yml` like the one below to the project root:

```
# To create: conda env create -f environment.yml
# To update: conda env update -f environment.yml --prune
name: <project_name>
channels:
  - conda-forge
  - nodefaults
dependencies:
  - python=3.10.*
  - pyopengl
  - pytorch::pytorch=1.12.0
  - pip
  - pip:
    - warp-lang

```

1. Run this from the project root:
    
    `conda env create -f environment.yml`
    
2. In PyCharm:
    - Preferences → Project: <project_name> → Python Interpreter
    - Add Interpreter → Add Local Interpreter…
    - Conda Environment → Interpreter: [select the newly created env]

## To Uninstall

`rm -rf ~/mambaforge ~/.conda`

(Optional, if not reinstalling): Edit ~/.zshrc to remove the Conda part.
