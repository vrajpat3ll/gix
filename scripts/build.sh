#!bin/sh
FILE="~/commands/commands.txt"
if [ ! -d "~/commmands" ]; then
    mkdir -p "~/commands"
fi
if [ ! -f "$FILE" ]; then
    touch "$FILE"
    cat <<EOF >> $FILE
git add .
git commit -m \$msg
git push
EOF
fi
pip install -r requirements.txt

pyinstaller --onefile main.py

pip uninstall -r requirements.txt

rm main.spec
rm -rf build
mv dist/main.* main.*
rm -rf dist