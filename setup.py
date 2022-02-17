from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="mcpi-blocks",
    version="1.0",
    description="A new block.py that has every block/item ID and some search functions to help you remember them all!",
    url="https://github.com/red-exe-engineer/Custom-MCPI-API",
    author="Red-Exe-Engineer",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["mcpi.data"],
    install_requires=["mcpi"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "mcpi-item-search = mcpi.data:main",
        ]
    },
)
