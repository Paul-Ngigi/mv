# Oslo Cinematix AS

## Setup/Installation Requirements
1. Move to the project folder and install requirements    
    * Create a virtual environment ```python3.8 -m venv virtual```
    * Activate the virtual environment ```source virtual/bin/activate```
    * Install application requirements ```pip install -r requirements.txt```
2.  Create the db on your local machine.  
    * Delete migrations file.
    * Open xampp server and start Apache and MYSQL.
    * Create a new database and name it ```cinema```.
    * Open config.py file and configure database username and password to your own user details.
    * Open terminal and check connection by typing the following commands :~
    * ```python3.8 manage.py shell```
    * Type ```db```. This command should display a response close to this ```<SQLAlchemy engine=mysql+pymysql://test:***@localhost/cinema?charset=utf8>``` to prove 
    connection is successfull.
    * Ctrl + Z to close python shell.
    * Initialize db ```python3.8 manage.py db init```
    * Make migrations ```python3.8 manage.py db migrate```
    * Upgrade the database ```python3.8 manage.py db upgrade```
3. Run main application   
   * Change app instance in manage.py to development ```create_app('development')```
   * Run on terminal ```python3.8 manage.py server``` or ```./start.sh```
   * Open on local browser ```http://127.0.0.1:5000/```

## Technologies Used
* MYSQL
* Flask framework
* Python3
* Bootstrap5
* HTML5

