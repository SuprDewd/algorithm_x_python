import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algorithm_x",
    version="0.1.0",
    author="Bjarki Ágúst Guðmundsson",
    author_email="suprdewd@gmail.com",
    description="An efficient implementation of Algorithm X",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SuprDewd/algorithm_x_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)

