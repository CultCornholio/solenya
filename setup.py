import setuptools

def get_long_description(path):
    try:
        with open(path, "r") as fh:
            return fh.read()
    except FileNotFoundError:
        return str()

setuptools.setup(
    name="solenya", 
    version="0.1.7",
    author="Artur Saradzhyan, Alex Martirosyan",
    author_email="cult.cornholio@gmail.com",
    description="Microsoft365 Device Code Phishing Framework",
    long_description=get_long_description("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/CultCornholio/solenya",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'sol = msph.__main__:main',                  
        ],       
    },
    install_requires=['aiohttp==3.7.1', 'peewee==3.14.4', 'colorful==0.5.4'],
    setup_requires=['aiohttp==3.7.1', 'peewee==3.14.4', 'colorful==0.5.4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)