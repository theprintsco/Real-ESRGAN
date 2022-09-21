from distutils.core import setup

setup(
    name='Real-ESRGAN',
    version='0.1.0',
    author='sberbank-ai',
    author_email='x@y.com',
    scripts=['realesrgan.py','rrdbnet_arch.py', 'main.py'],
    url='https://github.com/sberbank-ai/Real-ESRGAN',
    description='Real-ESRGAN',
    install_requires=open('requirements.txt').read()
)