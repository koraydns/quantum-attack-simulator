from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quantum-attack-simulator",
    version="1.0.2",
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
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Natural Language :: English",
    ],
    project_urls={
        "Source": "https://github.com/koraydns/quantum-attack-simulator",
        "Paper": "https://doi.org/10.5281/zenodo.17586868",  
        "Documentation": "https://github.com/koraydns/quantum-attack-simulator#readme"
    },
    entry_points={
        "console_scripts": [
            "quantum-sim=examples.bb84_example:main",
        ],
    },
    python_requires=">=3.7",
)



