from setuptools import setup, find_packages

setup(
    name="blogger",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        "fastapi",
        "uvicorn",
        # Add other dependencies from your requirements.txt
    ],
)
