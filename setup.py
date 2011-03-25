#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-paging',
    version=".".join(map(str, __import__('paging').__version__)),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/django-paging',
    install_requires=[
        'django-templatetag-sugar>=0.1',
    ],
    tests_require=[
        'unittest2',
        'django',
    ],
    test_suite='unittest2.collector',
    description = 'An efficient paginator that works.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
