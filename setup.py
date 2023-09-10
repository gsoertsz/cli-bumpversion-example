
from setuptools import setup, find_packages

setup(
    name="hello",
    version="0.4.4",
    packages=find_packages(),
    include_package_data=True,
    data_files=[],
    entry_points={
        'console_scripts': [
            'hello = hello.hello:main'
        ]
    },
    install_requires=['click']
)