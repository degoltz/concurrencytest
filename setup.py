
"""setup/install script for concurrencytest"""


import os
from setuptools import setup


setup(
    name='degoltzconcurrencytest',
    version='0.0.2',
    py_modules=['degoltzconcurrencytest'],
    install_requires=['python-subunit', 'testtools'],
    author='Corey Goldberg',
    author_email='cgoldberg _at_ gmail.com',
    description='testtools extension for running unittest suites concurrently',
    url='https://github.com/degoltz/concurrencytest',
    download_url='https://github.com/degoltz/concurrencytest',
    keywords='test testtools unittest concurrency parallel'.split(),
    license='GNU GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ]
)
