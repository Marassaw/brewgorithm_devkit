from setuptools import setup, find_packages
from os import path

setup(
  name='Brewgorithm',
  version='2.0.0',
  description='Machine Learning Library For Beer',
  url='git@github.com:ericzhao28/brewgorithm.git',
  author='Eric Zhao, Brewgorithm, and Contributors',
  author_email='elzhao@caltech.edu',
  license='MIT',
  classifiers=[
    'Development Status :: 2 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Machine Learning Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
  ],
  keywords='beer data ai machine_learning',
  packages=find_packages(exclude=['docs', 'tests']),
  install_requires=['keras', 'gensim', 'spacy', 'h5py', 'sense2vec']
)
