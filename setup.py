import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='codb',  
    version='1.0',
    scripts=['./codb'],
    author="Edwin Ariza",
    author_email="me@edwinariza.com",
    description="Database manager CLI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eadev/codb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "pymysql",
        "tk",
        "tabulate",
        "stdiomask"
    ]
 )
