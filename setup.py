import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='tqdm_multi_thread',
    version='0.4',
    author="Ran Lin",
    author_email="boydfd@gmail.com",
    description="A tqdm multi-thread helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boydfd/tqdm_multi_thread",
    packages=setuptools.find_packages(),
    install_requires=['tqdm'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)