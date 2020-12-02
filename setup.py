import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geosig-LeducV",
    version="0.1.0",
    author="Vincent Leduc",
    author_email="leduc232@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeducV/geosig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APPACHE 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires="lxml"
)
