
'''essential for packagin and distributing entire py project.
define configurations of project such as metadata dependencies and more'''

''' -e. is a reference to this setup.py file,it executes and the entire code here 
and makes sure to setup the entire python code as a package '''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Krish Naik",
    author_email="krishnaik06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)