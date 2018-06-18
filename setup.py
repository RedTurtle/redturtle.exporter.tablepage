# -*- coding: utf-8 -*-
"""Installer for the redturtle.exporter.tablepage package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='redturtle.exporter.tablepage',
    version='1.0a1',
    description="Exporter for redturtlet.exporter.base for collective.tablepage items",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='RedTurtle Technology',
    author_email='sviluppoplone@redturtle.it',
    url='https://pypi.python.org/pypi/redturtle.exporter.tablepage',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['redturtle', 'redturtle.exporter'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'plone.api',
        'setuptools',
        'collective.tablepage',
        'redturtle.exporter.base'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
