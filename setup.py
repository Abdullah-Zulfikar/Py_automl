from setuptools import setup, find_packages

setup(
    name="Py_automl",       # your package name (see below)
    version="0.1.0",
    author="Abdullah Zulfiqar",
    author_email="abdullahzulfiqar123apple@gmail.com",
    description="Automated ML assistant to analyze datasets and recommend models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/automl_assistant", 
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pycaret",
        "jinja2",
        "weasyprint",
        # add other dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
