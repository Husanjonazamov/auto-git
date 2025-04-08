from setuptools import setup, find_packages

setup(
    name="autogit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'jst-aicommit',
        'rich',
        
    ],
    entry_points={
        'console_scripts': [
            'autogit=auto_git.cli:aic',  
        ],
    },
    url="https://github.com/Husanjonazamov/auto-git",
    author="Husanjon Azamov",
    author_email="azamovhusanboy@gmail.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)