import re

from setuptools import setup, find_packages


(__version__, ) = re.findall(r"__version__.*\s*=\s*[\"]([^']+)[\"]",
                             open('easydata/__init__.py').read())


setup(
    name='easydata',
    version=__version__,
    description='Data transformation and manipulation library',
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    author='Rok Grabnar',
    author_email='grabnarrok@gmail.com',
    url='https://github.com/sitegroove/easydata',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'dateparser',
        'easytxt',
        'furl',
        'ftfy',
        'jmespath',
        'price-parser',
        'pyquery',
        'xmltodict'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
