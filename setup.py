from setuptools import find_packages, setup

setup(
    name='cardano_explorer',
    packages=find_packages(include=['cardano_explorer']),
    version='0.1.0',
    description='Python wrapper for accessing and processing information stored on the Cardano blockchain using Blockfrost API.',
    author='Djessy ATTA',
    license='MIT',
    install_requires=['pandas>=1.3.2', 'requests>=2.26.0', 'typing>=3.7.4.3', 'numpy==1.21.2'],
    tests_require=['pytest>=6.2.5', 'pytest-runner>=5.3.1'],
    test_suite='test_cardano_explorer',
)