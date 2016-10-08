from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
with open(path.join(path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='GitLabPy',
    version='0.4.1',
    py_modules=['GitLabPy'],
    description="A Python library to sort GitLab's Webhooks",
    long_description=long_description,
    author='Dixon Begay',
    author_email='dixonbegay@gmail.com',
    maintainer='Dixon Begay',
    url='https://github.com/dixon13/GitLabPy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.5'
    ],
    license='MIT',
    keywords='gitlabpy',
    install_requires=[]
)
