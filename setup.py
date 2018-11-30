import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name="hanako",
    version="0.0.1",
    author="BitolaHacklab",
    author_email="dev@bitolahacklab.org",
    description="Real time multiplayer game server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BitolaHacklab/Hanako",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Game Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries",
    ),
    install_requires=[
    ]
)
