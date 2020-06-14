# COMPACT - IIITA

![Compact](https://user-images.githubusercontent.com/66634743/84601944-ecd50e00-ae94-11ea-9387-abb05e4a5183.png)


Compact is a Python based website using the Django framework, this site aims to act as a central and common sourse for the Students of IIIT Allahabad.

You can find the Youtube Link to our project demonstration here : [Compact](https://www.youtube.com/watch?v=-uP4h10tBd4)

## Index:

1. [Installation](#installation)
2. [Code Execution](#code-execution)
3. [Database Prerequisites](#database-prerequisites)
4. [Testing](#testing)
5. [Team Info](#team-info)

## Installation:

### Basic Downloads Requirements - 

1. Python3 - Download howerve you wish 
2. Mysql - 
	* [MySQL](https://dev.mysql.com/doc/refman/8.0/en/linux-installation.html) (Download according to your decvice)
	* sudo apt-get install mysql-server (Download MySQL server)
	* After these downloads setup MySQL in you system however you please, This involves settup up the root password(if any)
3. pip3 - sudo apt-get install python3-pip
4. A hosting application, prefered XAMPP but you can use apache2 separately
	1. XAMPP comes pre-installed with 
		* MariaDB
		* PHP
		* Apache

To download [Apache](https://www.apachefriends.org/download.html) (choose your OS appropriately)

### Specific Downloads Requirements - 

1. Django - <br />
	pip install Django==3.0.5 (recommended version)
	
2. mysql client - <br />
	python -m pip install mysqlclient==1.4.2.post1


### Django Settup instructions:

The main file that you will need to settup is the **settings.py** file

```python
DATABASES = {
    'default': 
	{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MysqlDemo',		<- whatever the databases youhave
        'USER' : 'root',    		<- If you want root to access the database
        'PASSWORD' : '',		<- your MySQL password for user root
        'HOST' : 'localhost',
        'POST' : '',
    }
}
```

**Note: change only the marked information**

## Code Execution

### Usage 

To run this project you will need the following.
	
1. Navigate to the projectfile.
2. Now when you list the contents you sould see a file called manage.py
3. Then run the following commands
```console
foo@bar:~$ python manage.py makemigrations
foo@bar:~$ python manage.py migrate
foo@bar:~$ python manage.py runserver
```
Cnsidering all the commands ran smoothly, you are now ready to use the site. Go to your desired browser and type either of the two.

* 127.0.0.1:8000
* localhost:8000

## Database Prerequisites:

You will notice that you will not be able to sign in or use the site to its fullest, this occures because the **database is empty** at this point of time.

1. Do back to your terminal and type the following commands:
```console
foo@bar:~$ python manage.py createsuperuser
```

2. Fill in the required details and visit the following URL:<br />
```
localhost:8000/admin
```

This will take you to the admin panel where you can login as admin and poppulate the tables.

## Testing

For testing purposes you will need to fill only 
1. Users
2. Facultys
3. Teaches

Users table contains all the users that can login into the site, you will need to add the LDAP credentials eg,
```
      	USERNAME		EMAILADDRESS			FIRSTNAME		LASTNAME
	IIT2018179		iit2018179@iiita.ac.in		Mohammed		Aadil
	RK			rkala@iiita.ac.in		Rahul			Kala
	.				.			.			.
	.	 			.			.			.	
	.				.			.			.
```

Facultys table contains all the Faculty information,
you will need to add the CourseID and the ProfID eg,
```
	ProfID   : RK
	CourseID : IDAA
```

Teaches this table contains the courses available 
for the students of a specific year eg,
```
	ProfID : RV
	Course : ISOE
```

After you have filled these tables you are done with the settup process

## Team Info

For any furthur information on how to run the project, please contact any of the following:

1. [Milan A. Bhuva](https://github.com/MB557)
2. [Manav  Agrawal](https://github.com/mka2011)
3. [Mohammed Aadil](https://github.com/XXDIL)
4. [Ankit Rauniyar](https://github.com/Nkit-333)


