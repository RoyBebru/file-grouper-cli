from setuptools import setup, find_namespace_packages

setup(name='figro',
    python_requires='>=3.8',
    version='0.0.1',
    description='File Grouper (CLI). GOIT, HW #7',
    url='https://github.com/RoyBebru/file-grouper-figro',
    author='Roy Bebru',
    author_email='RoyBebru@Gmail.Com',   ### Script Name After Installation
    license='MIT',                       #       ### Import module which must be called
    include_package_data=True,           #       #           ### Function call from module
    packages=['figro'],                  #       #           #
    entry_points = {'console_scripts': 'figro = figro.figro:main'})
