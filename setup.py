from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        README = f.read()
    return README


setup(
    name="genclf",
    version="0.0.1",
    description="Gender Classifier ML Package for classifying gender using firstname",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Ankit Hemant Lade",
    author_email="ankitlade12@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["joblib", "scikit-learn"],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "genderclf": ["models/*.pkl"],
    },
)
