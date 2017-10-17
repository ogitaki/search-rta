from setuptools import setup

setup(
    name='ExposerDAI',
    version='1.0',
    author='Ognyan Stoimenov',
    packages=['exposer_dai'],
    install_requires=['requests', 'progressbar2'],
    entry_points={
        'console_scripts': ['run = exposer_dai.app:main']
    }

)
