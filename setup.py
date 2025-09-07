from setuptools import setup, find_packages


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='OpenPartsLibrary-Föasl',
    version='0.1.0',    
    description='Flask Extension for managing a parts library of hardware components for manufacturing in a web application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alekssadowski95/OpenPartsLibrary-Flask',
    author='Aleksander Sadowski',
    author_email='aleksander.sadowski@alsado.de',
    license='MIT',
    packages=find_packages(),
    install_requires=['sqlalchemy', 'datetime', 'pandas', 'openpyxl'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3'
    ],
)
