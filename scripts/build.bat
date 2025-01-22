pip install -r requirements.txt

pyinstaller --onefile gitpush.py

pip uninstall -r requirements.txt

rm gitpush.spec
rm -rf build
mv dist/gitpush* gitpush.exe
rm -rf dist