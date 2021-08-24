import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pentools", 
    version="0.0.1",
    author="Artur Saradzhyan, Alex Martirosyan",
    author_email="",
    description="CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/msphish",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'msphish = msphish.__main__:main',                  
        ], 
        'msphish.registered_commands': [
            'devc = msphish.commands.devc:main',
            'tokens = msphish.commands.tokenst:main'
        ]         
    },
    install_requires=['requests'],
    setup_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)