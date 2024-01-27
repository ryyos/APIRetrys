from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'To handle API request retries due to timeouts'
LONG_DESCRIPTION = 'Are you annoyed because your request has an error due to internet problems ? I think this could be the answer'

# Setting up
setup(
    name="ApiRetrys",
    version=VERSION,
    author="ryyos (Rio Dwi Saputra)",
    author_email="<riodwi12174@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['logging', 'requests'],
    keywords=['python', 'requests', 'retry', 'api', 'timeout', 'auto', 'session'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: Microsoft :: Windows",
    ]
)