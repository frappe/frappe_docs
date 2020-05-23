# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappeframework_com/__init__.py
from frappeframework_com import __version__ as version

setup(
	name='frappeframework_com',
	version=version,
	description='Website and Documentation for Frappe Framework',
	author='Frappe Technologies',
	author_email='developers@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
