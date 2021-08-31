import setuptools

def get_long_description(path):
    try:
        with open(path, "r") as fh:
            return fh.read()
    except FileNotFoundError:
        return str()

setuptools.setup(
    name="msph", 
    version="0.1.4",
    author="Artur Saradzhyan, Alex Martirosyan",
    author_email="",
    description="CLI tool",
    long_description=get_long_description("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/msph",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'msph = msph.__main__:main',                  
        ],       
    },
    install_requires=['aiohttp', 'peewee', 'colorful'],
    setup_requires=['aiohttp', 'peewee', 'colorful'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)