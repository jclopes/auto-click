@echo off
echo Starting install...
echo
python -m venv env
call env\Scripts\activate && pip install -r requirements.txt
echo
echo Installation completed!
pause
