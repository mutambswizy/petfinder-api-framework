from setuptools import setup, find_packages

setup(
    name="petfinder-api-framework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pytest",
        "responses",
    ],
)