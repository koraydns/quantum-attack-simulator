from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="quantum-attack-simulator",  
    version="1.0",  
    author="Koray Danisma",  
    author_email="koray.danisma@gmail.com",  
    description="A Python library for simulating BB84 protocol security and attacks.",
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    url="https://github.com/koraydns/quantum-attack-simulator",
    packages=find_packages(),  
    install_requires=[
        "qiskit>=0.45.0",
        "qiskit-aer>=0.13.1",
        "matplotlib>=3.8.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",  
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    entry_points={
        "console_scripts": [
            "quantum-sim=examples.bb84_example:main",
        ],
    },
    python_requires=">=3.7"
)
