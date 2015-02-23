#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='nameko',
    version='2.0.0',
    description='A microservices framework for Python that lets service '
                'developers concentrate on application logic and encourages '
                'testability.',
    author='onefinestay',
    author_email='nameko-devs@onefinestay.com',
    url='http://github.com/onefinestay/nameko',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        "eventlet",
        "kombu<=3.0.4",
        "mock",
        "path.py>=6.2",
        "pyrabbit",
        "Werkzeug",
    ],
    extras_require={
        'dev': [
            "coverage==4.0a1",
            "flake8==2.1.0",
            "mccabe==0.3",
            "pep8==1.6.1",
            "pyflakes==0.8.1",
            "pylint==1.0.0",
            "pytest==2.4.2",
            "pytest-timeout==0.4",
            "requests==2.5.0",
            "websocket-client==0.23.0",
        ],
        'docs': [
            "pyenchant==1.6.6",
            "Sphinx==1.2",
            "sphinxcontrib-spelling==2.1.1",
            "sphinx-rtd-theme==0.1.6",
        ],
    },
    entry_points={
        'console_scripts': [
            'nameko=nameko.cli.main:main',
        ],
    },
    zip_safe=True,
    license='Apache License, Version 2.0',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ]
)
