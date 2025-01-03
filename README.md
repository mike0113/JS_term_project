## Getting Started

### 1. Clone the repository:
You can clone the repository using the following command:
```bash
git clone git@github.com:mike0113/JS_term_project.git
cd JS_term_project
```

### 2. Set up a Python Virtual Environment
It's recommended to use a Python virtual environment to isolate project dependencies. Choose the appropriate set of commands based on your operating system:
#### linux
```bash
python3 -m venv .venv
. ./.venv/bin/activate
```
#### windows
```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
```

### 3. Install Required Packages
Install the required Python packages by running the following command:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Server
Now, you can start the Flask development server with the following command:
```bash
python search.py
```

### 5. Open the frontend
open search.html on browser


-------------------------

In database, there already has two data:

1. name = 秋紅谷, city = 台中市

2. name = 暨南大學, city = 南投縣

So you can search these two data.

Or you may use `sqlite3` to manual add it.

----------------------

This is a simple version of search lands backend and a little frontend.

And I am learning some skill from Flask such as Blueprint, JWT token ...

