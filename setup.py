from distutils.core import setup

setup(
    name = "fsmonitor",
    version = "0.1",
    description = "Filesystem monitoring",
    author = "Luke McCarthy",
    author_email = "luke@iogopro.co.uk",
    url = "http://github.com/shaurz/fsmonitor",
    install_requires=[
        'pypiwin32',
    ],
    packages = ["fsmonitor"],
)
