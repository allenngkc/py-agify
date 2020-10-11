import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-agify", # Replace with your own username
    version="0.0.1",
    author="Allen Ng",
    author_email="pikachuexeallen@gmail.com",
    description="A python wrapper for agify, genderize, nationalize API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allenng321/py-agify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)