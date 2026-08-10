if [ -d "htmlcov" ]; then
    echo "Removing htmlcov Dir"
    rm -rf htmlcov
fi

if [ -f ".coverage" ]; then
    echo "Removing Coverage File"
    coverage erase
fi

echo "Running Tests With Coverage"
coverage run --source=nptdms -m unittest discover
coverage run -a -m behave

echo "Generating HTML Coverage"
coverage html --omit="*/nptdms/tests/*,*/nptdms/test/*,*/nptdms/export/*,*/nptdms/version.py,*/nptdms/__init__.py"
coverage report -m --omit="*/nptdms/tests/*,*/nptdms/test/*,*/nptdms/export/*,*/nptdms/version.py,*/nptdms/__init__.py"
echo "Done"