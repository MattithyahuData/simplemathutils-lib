from setuptools import setup, find_packages

# Reading in README as text for description 
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Versioning and Description 
VERSION = '0.1.2'
DESCRIPTION = 'simplemathutils-lib is a creative package for basic mathematical operations with Python.'


CLASSIFIERS = [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Typing :: Typed",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
                ]

setup(
        name="simplemathutils_lib", 
        version=VERSION,
        author="Mattithyahu O",
        author_email="contactmattithyahu@gmail.com",
        url="https://github.com/MattithyahuData/simplemathutils-lib",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[], 
        keywords=['math'],
        classifiers= CLASSIFIERS,
        python_requires=">=3.6",
)


