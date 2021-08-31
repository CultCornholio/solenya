cd ..
python setup.py install
yes | pip uninstall msph
rm -rf dist/
rm -rf build/
rm -rf msph.egg-info/
python setup.py install
rm -rf dist/
rm -rf build/
rm -rf msph.egg-info/
