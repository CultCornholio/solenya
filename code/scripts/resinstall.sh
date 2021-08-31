cd ..
python setup.py install
yes | pip uninstall pentools
rm -rf dist/
rm -rf build/
rm -rf pentools.egg.info/
python setup.py install