from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filed_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(filed_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements       

setup(
    name='MLPROJECT',
    version='0.0.1',
    author='mani',
    author_email='thotamaniraju18@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
