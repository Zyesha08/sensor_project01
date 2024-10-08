from setuptools import find_packages,setup   ##setuptools is a package that provides tools for python 
from typing import List

hyphen_e_dot = '-e.'

def get_requirements(file_path:str)->List[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    if hyphen_e_dot in requirements:
        requirements.remove(hyphen_e_dot)
    return requirements


setup(
    name = 'Fault detection',
    version='0.0.1',
    author = 'sakshi',
    author_mail = 'arya.sakshi96@gmail.com',
    install_requirements =get_requirements('requirements.txt'),
    packages=find_packages()
)