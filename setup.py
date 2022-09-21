from distutils.core import setup

setup(
    name="REAL_ESRGAN_FORK",
    version="0.1",
    author="theprintsco",
    author_email="contact@theprintscompany.com",
    packages=["Real-RealESRGAN"],
    install_requires=[numpy, 
    opencv-python,
    Pillow,
    torch>=1.7,
    torchvision>=0.8.0,
    tqdm,
    imageio,]
)