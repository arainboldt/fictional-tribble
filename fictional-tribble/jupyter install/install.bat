@echo off

python ./get-pip.py
pip install https://github.com/arainboldt/fictional-tribble@main
python ./create_jupyter_home.py

pause
exit