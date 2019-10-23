from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements


def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]


setup(
    name="PythonJsonEditorWindow",
    version="0.0.1",

    # metadata to display on PyPI
    author="starikcetin <cetinsamedtarik@gmail.com> (https://github.com/starikcetin)",
    author_email="cetinsamedtarik@gmail.com",
    description="A GUI window for editing JSON files using Python.",
    keywords="python json editor window gui ui",
    url="https://github.com/starikcetin/PythonJsonEditorWindow",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt"),
)
