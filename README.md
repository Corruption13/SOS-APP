# S.O.S Disaster Management Framework

> *Securing Today, to Rebuild Tomorrow* 

A Web-App Framework based on Django for managing disasters all over the world.


## Concept

The idea of this framework's is to provide a base platform on top of which goverment agencies and other organisations can quickly build services to coordinate rescue efforts for any disaster or catastrophic event. We provide a base set of features such as a victim map and rescue team system, which can be further extended to meet the requirements of the specific situation at hand. 

 ## Installation Process
	
	-> Install Python 3.9 
	
	$ pip install -r requirements.txt
	optional: $ python manage.py createsuperuser
	$ python manage.py migrate
	$ python manage.py runserver
	
	-> open localhost:8000 on browser


## Stock webpages provided

#### User Landing Page

![Initial landing page](https://github.com/raksha-oss/SOS-APP/blob/master/project-images/sos-menu.png?raw=true)


#### User

![Rescue me page](https://github.com/raksha-oss/SOS-APP/blob/master/project-images/sos-map-rescue.png?raw=true)

#### Rescue Team View 

![Victim Map](https://github.com/raksha-oss/SOS-APP/blob/master/project-images/sos-victim-map.png?raw=true)

#### Victim Detail View

![Victim Detail](https://github.com/raksha-oss/SOS-APP/blob/master/project-images/sos-victim-map-details.png?raw=true)









> **Note**: Do not actually use this for real life events, as this is a proof of concept that has not been tested for scalability or reliability in a real world environment.
