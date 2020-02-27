import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moses_crossval",
    version="0.1",
    author="Abdulrahman Semrie",
    author_email="hsamireh@gmail.com",
    description="A tool to run cross-validation using moses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Habus/moses-crossval",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)