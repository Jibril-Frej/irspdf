import sys
from unittest.mock import MagicMock


# -- Options for import C dependant libraries
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = ['numpy']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'irspdf'
copyright = '2021, Jibril Frej'
author = 'Jibril Frej'

release = '0.3'
version = '0.3.5'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
