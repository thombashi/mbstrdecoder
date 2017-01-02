# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

import io
import os.path
import setuptools
import sys


needs_pytest = set(["pytest", "test", "ptr"]).intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []


REQUIREMENT_DIR = "requirements"

with io.open("README.rst", encoding="utf8") as f:
    long_description = f.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_require = [line.strip() for line in f if line.strip()]

setuptools.setup(
    name="mbstrdecoder",
    version="0.2.1",
    author="Tsuyoshi Hombashi",
    author_email="gogogo.vm@gmail.com",
    url="https://github.com/thombashi/mbstrdecoder",
    keywords=["multi-byte character", "unicode", "decoder"],
    license="MIT License",
    description="multi-byte character string decoder",
    long_description=long_description,
    include_package_data=True,
    install_requires=install_requires,
    packages=setuptools.find_packages(exclude=["test*"]),
    setup_requires=pytest_runner,
    tests_require=tests_require,

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
