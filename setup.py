from distutils.core import setup

setup(
    name='eve-verbose-killmail',
    version='0.1.2',
    packages=['eve_verbose_killmail'],
    package_dir={'eve_verbose_killmail': 'src/eve_verbose_killmail'},
    package_data={'eve_verbose_killmail': ['ressources/*.csv']},
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    author='Leon Hess',
    author_email='leon.hess@mailbox.tu-dresden.de',
    url='https://github.com/leonhess/eve-verbose-killmail',
    install_requires=[
        'requests'
    ],
    download_url='https://github.com/leonhess/eve-verbose-killmail/releases/download/v0.1.1/eve-verbose-killmail-0.1.2.tar.gz'
)
