from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in common_features_v14/__init__.py
from common_features_v14 import __version__ as version

setup(
	name="common_features_v14",
	version=version,
	description="Common Features",
	author="Thirvusoft",
	author_email="thirvusoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
