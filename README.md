# CSGO-task
Task assigned for CSGO

#installation steps

#to install virtual env if not installed
pip install virtualenv 

#create virtual env with name myenv
python -m venv myenv  

#activate virtual env
myenv\Scripts\activate

#to use if venv does not activate
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process

#install 
pip install pytest-playwright mailosaur bs4

#dependencies
pip freeze > requirements.txt

#run test
pytest name of file


#for cross broswer test
--headed --browser webkit --browser firefox --browser chromium
pytest .\ui_test.py  --headed --device="iPhone 13"
