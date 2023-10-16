import setuptools

setuptools.setup(
    name="my_package",
    version="1.0.0",
    author="John Doe",
    description="A description of my package",
    packages=setuptools.find_packages(),
    install_requires=["numpy==1.26.1"],
)
