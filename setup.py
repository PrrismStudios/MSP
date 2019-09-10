import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MultiWii",
    version="0.0.1",
    author="Yuma (Prrism)",
    author_email="yumatezu@gmail.com",
    description="Python3 implementation of the Multi Serial Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PrrismStudios/MSP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pySerial>=3.4",
        "MultiWii"
    ],
    python_requires='>=3.7',
)