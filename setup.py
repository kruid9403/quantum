from setuptools import setup, find_packages

setup(
    name="quantum",
    version="0.1",
    description="A low level quantum computing library",
    author="Jeremy Kruid",
    author_email="jeremy@jeremykruid.io",
    packages=find_packages(),
    install_requires=[
    ],
    extras_require={
        "dev": [],
    },
    classifiers=[
        "Programming Language:: Python :: 3",
        "Operating System :: OS Independent",
         ],
    include_package_data=True,
    zip_safe=False,
)