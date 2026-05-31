# Python Project Quick Start

## short version:
```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
```

## 1. Create project

```bash
mkdir my-project
cd my-project
code .
```

## 2. Create virtual environment

```bash
python -m venv .venv
```

## 3. Activate virtual environment

Git Bash (Windows):

```bash
source .venv/Scripts/activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

You should now see:

```bash
(.venv)
```

in the terminal.

to stop: 
```bash
deactivate
```

## 4. Create project files

```bash
touch main.py README.md .gitignore
```

`.gitignore`

```gitignore
.venv/
__pycache__/
*.pyc
```

## 5. Install packages when needed

Example:

```bash
pip install requests
```

## 6. Save dependencies

```bash
pip freeze > requirements.txt
```

## 7. Run project

```bash
python main.py
```

## Daily workflow

Open project:

```bash
cd my-project
source .venv/Scripts/activate
python main.py
```

## Clone existing project

```bash
git clone <repo>
cd <repo>

python -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt
```
