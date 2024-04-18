from setuptools import setup, find_packages

setup(
    name = "hotdoc_my_extension",
    version = "0.8",
    keywords = "hotdoc",
    author_email = 'mathieu.duponchelle@centricular.com',
    license = 'LGPL',
    description = "An extra extension",
    author = "Mathieu Duponchelle",
    entry_points = {'hotdoc.extensions': 'get_extension_classes = my_extension.my_extension:get_extension_classes'},
)
