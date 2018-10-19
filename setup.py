from distutils.core import setup

setup(
    name='eve-verbose-killmail',
    version='0.1',
    packages=['eve_verbose_killmail'],
    package_dir={'eve_verbose_killmail': 'src/eve_verbose_killmail'},
    package_data={'eve_verbose_killmail': ['ressources/*.csv']},
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    author='Leon Hess',
    author_email='',
    url='',
    install_requires=[
        'requests'
    ],
)
