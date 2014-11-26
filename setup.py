from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksGeoserverManager',
    version='0.0.1',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks library to manage Geoserver clusters.',
    install_requires=[
        'gsconfig'
    ],
    url='http://pypi.python.org/pypi/GeobricksGeoserverManager/',
    keywords=['geobricks', 'geoserver', 'gis', 'gsconfig']
)
