# Chaos

Chaos is a simple game demonstrating graphical python code using [Kivy](https://github.com/kivy/kivy).

To edit the game, I recommend downloading [Atom](https://atom.io/)

To run on Windows, do the following.

1. Download [Python](https://www.python.org/downloads/) The 3.6.3 version is fine.
2. Install Python

Once python is installed, open a command prompt and check the following

1. To verify python is installed and working, type `python` at the prompt. If it launches correctly, python is installed.
2. Run the following commands:
```
python -m pip install --upgrade pip wheel setuptools

python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

python -m pip install kivy
```
3. Now you should be able to run chaos at the command prompt by typing `python chaos.py`
