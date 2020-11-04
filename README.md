# python-django-onion
### Overview
onion structure written in python and django


### Spec
```
Python==3.9.0
Django==3.1.2
SQLite3
```


### Installation
```pip install -r requirements.txt```


### Scenario
customer can order coffee to cafe


### Structure
* domain model: Entity. No dependency.
* object service : Simple jobs to control objects coming from domain model.
* application service : application service orchestrate specific business scenario.
* models: Django ORM based database access layer.
* serializer: Serialize or Deserialize data in and out from internal and external world.
* views: UI layer.
* tests: test layer.





