from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='debman',
      version=version,
      description="apt frontend with pacman syntax",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='apt ubuntu debian pacman',
      author='Vladimir Yakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/debman',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={'console_scripts': ['debman=debman:main']},
      )
