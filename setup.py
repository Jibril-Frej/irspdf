from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.3.4'
DESCRIPTION = 'A simple information retrieval system for pdf documents'


setup(
    name='irspdf',
    version=VERSION,
    author='Jibril Frej',
    author_email="<frejjibril@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={"Source code": "https://github.com/Jibril-Frej/irspdf"},
    packages=['irspdf'],
    install_requires=['numpy', 'pdfplumber', 'stop_words', 'snowballstemmer'],
    keywords=['python', 'information retrieval'],
    classifiers=['Programming Language :: Python :: 3']
)
