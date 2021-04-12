#nsml: nsml/default_ml:cuda9_torch1.0
from distutils.core import setup
import setuptools

setup(
    name='ncc_test',
    version='1.1',
    install_requires=['scikit-learn' ,'torch==1.3.1', 'matplotlib','opencv-python', 'efficientnet_pytorch',]
)
