from setuptools import find_packages, setuptools

try:
    with open('PYPI_README.md') as f:
        long_description = f.read()
except Exception as e:
    long_description=""

setuptools.setup(
    name='cardano_explorer',
    packages=find_packages(include=['cardano_explorer']),
    version='0.2.0',
    description='Python wrapper for accessing and processing information stored on the Cardano blockchain using Blockfrost API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Djessy ATTA',
    author_email = 'djessyatta@live.fr',
    url = 'https://github.com/djessy-atta/py-cardano-explorer',
    download_url = 'https://github.com/djessy-atta/py-cardano-explorer/archive/refs/tags/v0.2-beta.0.tar.gz',
    keywords = ['CARDANO', 'API', 'WRAPPER', 'BLOCKCHAIN', 'BLOCKFROST'],
    license='MIT',
    install_requires=['pandas>=1.3.2', 'requests>=2.26.0', 'typing>=3.7.4.3', 'numpy==1.21.2', 'tqdm>=4.62.2'],
    tests_require=['pytest>=6.2.5', 'pytest-runner>=5.3.1', 'tqdm>=4.62.2'],
    test_suite='test_cardano_explorer',
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',      
  ],
)

