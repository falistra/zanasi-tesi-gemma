# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Museo Gemma: indagine statistica conoscitiva sui frequentatori'
copyright = '2022, Fausto Zanasi'
author = 'Fausto Zanasi'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

autosummary_generate = True

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

html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_logo = "survey.png"
html_show_sourcelink = False

html_theme_options = {
    'logo_only': False,
    'display_version': False,
    'navigation_depth': 5,
    }

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

latex_elements = {
    'utf8extra':   ('\\ifdefined\\DeclareUnicodeCharacter\n'
                        ' \\ifdefined\\DeclareUnicodeCharacterAsOptional\\else\n'
                        '  \\DeclareUnicodeCharacter{1D6D8}{\\nobreakspace}\n'
                        '  \\DeclareUnicodeCharacter{03C7}{\\nobreakspace}\n'
                        '  \\DeclareUnicodeCharacter{274C}{\\nobreakspace}\n'
                        '\\fi\\fi'),
}
