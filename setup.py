import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="create-wheel",
    version="0.0.1",
    author="Gabriel Cánepa",
    description="Package to demonstrate how to create a wheel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.10',
)