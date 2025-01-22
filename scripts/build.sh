#!bin/sh
pip install -r requirements.txt

pyinstaller --onefile gitpush.py

pip uninstall -r requirements.txt

rm gitpush.spec
rm -rf build
mv dist/gitpush.* gitpush.*
rm -rf dist