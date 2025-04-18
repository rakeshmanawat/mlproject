##setup.py is a Python file, the presence of which is an indication that the module/package you are about to install has likely been packaged and distributed with Distutils, which is the standard for distributing Python Modules.

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the requirements.txt file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines from the file
        requirements = file_obj.readlines()

    # Remove newline characters and unnecessary items
    requirements = [req.strip() for req in requirements]

    # Remove the '-e .' entry if present
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Rakesh',
    author_email='rseervi329@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
