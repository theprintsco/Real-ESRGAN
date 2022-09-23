from distutils.core import setup

setup(
    name='Real-ESRGAN',
    version='0.1.0',
    author='sberbank-ai',
    author_email='x@y.com',
    url='https://github.com/sberbank-ai/Real-ESRGAN',
    description='Real-ESRGAN',
    install_requires=open('requirements.txt').read()
    py_modules=['realesrgan', 'rrdbnet_arch', 'main', 'arch_util', 'utils_sr']
)
