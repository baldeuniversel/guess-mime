from setuptools import setup, find_packages





setup(
    name="guess-mime",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["python-magic"],
    entry_points={
        "console_scripts": [
            "guess-mime=main:main",
        ],
    },
    author="Amadou Baldé (baldeuniversel@protonmail.com)",
    description="Detects the MIME type of a file",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
