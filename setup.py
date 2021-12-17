from setuptools import setup

VERSION = '0.2.7'
DESCRIPTION = 'Information retrieval system for pdf documents'


setup(
    name='irspdf',
    version=VERSION,
    author='Jibril Frej',
    author_email="<frejjibril@gmail.com>",
    description=DESCRIPTION,
    packages=['irspdf'],
    install_requires=['numpy', 'pdfplumber', 'stop_words'],
    keywords=['python', 'information retrieval'],
    classifiers=[
        'Programming Language :: Python :: 3'
        ]
)
