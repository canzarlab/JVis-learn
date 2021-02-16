# a. Delete all files in the dist folder.
#
# b. Update the version number in the setup.py file.
#
# c. Re-create the wheels:
#
# python3 setup.py sdist bdist_wheel
# d. Re-upload the new files:
#
# twine upload dist/*

python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*
