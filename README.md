# djn-rct-wbp-base
This project helps you to create a work environment to work with:
* Django 2.* 
* ReactJs 16.* 
* Webpack 4.* 

## Getting Started
This app cames with two basic folders:
* *Backend*: Where Django sources lives.
* *Frontend*: All your ReactJS sources should be here.
#### Prerequisites
You need a virtual environment with python 3.6 and npm 6.4 (at least)
#### Installation
1. Download the code from github repository [djn-rct-wbp-base](https://github.com/luko82/djn-rct-wbp-base/archive/master.zip)

2. Create a virtual environment (the route depends on your preferences)
```
$ cd /{route-to-your-environment-folders}
$ mkdir {my-new-environment}
$ cd {my-new-environment}
$ virtualenv -p python3.6 .
```
3. Activate your new environment and install necessary python packages with pip.
```
$ cd {your-prj-route}
$ bash {route-to-your-new-environment}/bin/activate
$ pip install -r backend/requirements/base.txt
```
4. Once it has finished, create the Django environment
```
$ backend/manage.py makemigrations
$ backend/manage.py migrate
```
Note:
1. Your django settings secret key should be created at the end of your "activate" script in your virtualenv. 
5. Install npm packages
```
$ cd frontend
$ npm install
```

