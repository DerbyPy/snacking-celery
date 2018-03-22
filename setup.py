import os.path as osp

from setuptools import setup, find_packages

cdir = osp.abspath(osp.dirname(__file__))
README = open(osp.join(cdir, 'readme.rst')).read()
CHANGELOG = open(osp.join(cdir, 'changelog.rst')).read()

version_fpath = osp.join(cdir, 'snacking', 'version.py')
version_globals = {}
with open(version_fpath) as fo:
    exec(fo.read(), version_globals)

setup(
    name='Snacking on Celery',
    version=version_globals['VERSION'],
    description='<short description>',
    long_description='\n\n'.join((README,)),
    author='Randy Syring',
    author_email='randy.syring@level12.io',
    url='https://github.com/derbypy/snacking-celery',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # use this for libraries; or
        # use requirements folder/files for apps
        'click',
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['restview', 'flake8'],
        'test': ['pytest'],
    },
    entry_points='''
        [console_scripts]
        snacking = snacking.cli:cli_entry
    ''',
)
