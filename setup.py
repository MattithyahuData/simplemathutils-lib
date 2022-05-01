from setuptools import setup, find_packages
from git import Repo

# Initialising repository
repo = Repo()

# Getting number of commits 
commits = len(list(repo.iter_commits()))

# Dividing number of commits by 100 
verse = float(commits/100) 

# Incrementing version by 0.01
version = verse + 0.01

VERSION = f'{version}' 
DESCRIPTION = 'Python package 1.0'
LONG_DESCRIPTION = 'Math -----'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="simplemathutils_lib", 
        version=VERSION,
        author="Mattithyahu O",
        author_email="contactmattithyahu@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'math'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)