# -*- coding: utf-8 -*-
import os.path
import subprocess
import sys

from setuptools import setup
from setuptools.command.install import install as _install


def get_pwd_candidates():
    """attempt to get a working directory for running `pre-commit install` in.

    - pip installs in a temporary directory so `os.getcwd()` won't work
    - `$PWD` is likely to work, but won't work on windows
    - `$VIRTUAL_ENV` probably works, if your virtualenv is in your git repo
    - `os.path.dirname(sys.executable)` is another potential option
    """
    for v in ('PWD', 'VIRTUAL_ENV'):
        if os.environ.get(v):
            yield os.environ[v]
    yield os.path.dirname(sys.executable)


class install(_install):
    def run(self):
        _install.run(self)
        for pwd in get_pwd_candidates():
            cmd = (sys.executable, '-m', 'pre_commit', 'install')
            if not subprocess.call(cmd, cwd=pwd):
                return
        else:
            raise SystemExit(r'wellp, I tried ¯\__(ツ)__/¯')


try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def run(self):
            raise SystemExit('this is fine')
except ImportError:
    bdist_wheel = None


setup(
    name='pre-commit-installed',
    description='runs `pre-commit install` on installation (terrible hack)',
    long_description='this is a terrible hack, probably do not use in prod',
    long_description_content_type='text/markdown',
    url='https://github.com/pre-commit/pre-commit-installed',
    version='0.0.1',
    author='Anthony Sottile',
    author_email='asottile@umich.edu',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=['pre-commit'],
    cmdclass={'bdist_wheel': bdist_wheel, 'install': install},
)
