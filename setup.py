from setuptools import setup, find_packages

setup(
    name="code-formatter-pro-golang-20260527_011923",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'code=code:main',
        ],
    },
)
