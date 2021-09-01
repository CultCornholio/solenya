cd ..
rm -rf build
rm -rf dist
rm -rf .egg-info
rm -rf eggs
python setup.py sdist bdist_wheel
twine upload dist/*