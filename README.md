INSTALLING</br></br>

Backend:</br>
  --- create environment</br>
  --- pull project from git</br>
  --- install denpendecies from requirments.txt</br>
  --- create database</br>
  --- configurate local_settings.py using settings_local</br>
  --- make migrations and migrate</br>
  --- add to db valutes and rates using managment commands:</br>
        &emsp;&emsp;-- get_valutes</br>
      &emsp;then</br>
        &emsp;&emsp;-- get_valute_rates</br></br>
        
Frontend:</br>
  --- install packeges using YARN or NPM</br>
  If not started django on localhost:8000:</br>
  --- configurate Axios.defaults.baseURL in front/src/main.js</br></br>
  
 
RUNNING</br></br>
 
Backend:</br>
  --- add management command for taken valute_rates to CronTab</br>
  --- python manage.py runserver</br></br>
  
Frontend:</br>
  --- npm run serve</br>
