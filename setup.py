from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirements_list=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e.":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt was not found")
    return requirements_list

setup(
    name= "network_security",
    version= "0.0.1",
    author="surya",
    author_email="suryatejak@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)




