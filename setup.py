from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='hadoop_tools',
      version=version,
      description="some tools for upload file to hadoop",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='hadoop rq',
      author='@timger',
      author_email='yishenggudou@gmail.com',
      url='http://www.timger.info/about',
      license='QIYI',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
