from distutils.core import setup

setup(
    name='TowelStuff',
    version='0.1.0',
    author='J. Random Hacker',
    author_email='jrh@example.com',
    scripts=['realesrgan.py','rrdbnet_arch.py', 'main.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    description='Useful towel-related stuff.',
    install_requires=open('requirements.txt').read()
)