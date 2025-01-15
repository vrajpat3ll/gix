pip install -r requirements.txt

pyinstaller --onefile gitpush.py

rm gitpush.spec
rm -rf build
mv dist/gitpush.exe gitpush.exe
rm -rf dist