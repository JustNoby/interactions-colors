from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="interactions-colors",
    version="0.1",
    description="Add a color function to Embed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JustNoby/interactions-colors",
    author="JustNoby",
    author_email="justnobodysilver@gmail.com",
    license="MIT",
    packages=["interactions.ext.colors"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "discord-py-interactions>=4.1.0"
    ],
)