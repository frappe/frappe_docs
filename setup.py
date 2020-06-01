# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_docs/__init__.py
from frappe_docs import __version__ as version

setup(
	name='frappe_docs',
	version=version,
	description='Frappe Framework Documentation',
	author='Frappe Technologies',
	author_email='developers@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
