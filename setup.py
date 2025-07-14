from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines() #output:requirements = ['openai', 'langchain', 'transformers']

setup(
    name="RAG Medcal Chatbot",
    version="0.1",
    author="Sudhanshu",
    packages=find_packages(), #Auto-include all folders that are Python packages 
    install_requires = requirements,
)

'''
**`setuptools`** library (a standard tool for building and packaging Python projects)
- `setup()` — the main function that defines your project.
- `find_packages()` — automatically finds all Python packages (folders with `__init__.py` in them) to include.



'''