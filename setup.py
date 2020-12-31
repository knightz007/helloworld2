from setuptools import setup

with open("README.md","r") as rd:
    long_description = rd.read()

setup(
    name="helloworld2",
    version='0.0.1',
    description='Say hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["helloworld2"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    url="https://github.io/knightz007/helloworld2",
    author="Anup Kumar",
    author_email="anupkumar.menon@yahoo.com",
)