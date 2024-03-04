from setuptools import find_packages, setup
from typing import List

endline='-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if endline in requirements:
            requirements.remove(endline)

    return  requirements


setup(
    name="ML_project",
    version='0.0.1',
    author="Ajeesh",
    author_email="ajeeshperalayil@gmail.com",

    packages=find_packages(),
    include_dirs=get_requirements('requirements.txt')
)
