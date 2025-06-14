import pathlib
from setuptools import setup, find_packages

DISTRIBUTION_NAME = "configs"
THIS_DIR = pathlib.Path(__file__).parent
LONG_DESCRIPTION = (THIS_DIR / "README.md").read_text()

setup(
    name=DISTRIBUTION_NAME,
    version='0.1.8',
    description="A collection of sinontop utilities and configurations.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Sintacs Ao",
    author_email="sinontop.gleeze.com",
    license="MIT",
    url="https://t.me/sinontop",
    zip_safe=False,
    project_urls={"GitHub": "https://github.com/sintxcs/configs"},
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: MIT License',
        'Programming Language :: Python :: 3'
    ],
)
