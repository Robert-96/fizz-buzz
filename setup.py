from setuptools import setup, find_packages


NAME = 'fizz-buzz'
VERSION = '0.1.0'
DESCRIPTION = 'Fizz-Buzz is a group word game for children to teach them about division.'
URL = 'https://github.com/Robert-96/fizz-buzz/'
EMAIL = 'dezmereanrobert@gmail.com'
AUTHOR = 'Robert-96'
REQUIRES_PYTHON = '>=2.7.0'
LICENSE = 'MIT'

PROJECT_URLS = {
    'Bug Tracker': 'https://github.com/Robert-96/fizz-buzz/issues/',
    'Documentation': 'https://github.com/Robert-96/fizz-buzz/blob/main/README.md/',
    'Source': 'https://github.com/Robert-96/fizz-buzz/'
}

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

with open('README.md') as f:
    README = f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    license=LICENSE,
    url=URL,
    project_urls=PROJECT_URLS,

    author=AUTHOR,
    author_email=EMAIL,

    python_requires=REQUIRES_PYTHON,
    setup_requires=REQUIRED,
    install_requires=REQUIRED,
    packages=find_packages(exclude=['tests']),

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Cython',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Operating System :: OS Independent',
    ],
    keywords='fizz-buzz',
)