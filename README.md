# ClearDataTest
*Software Engineer Assessment Test: You will receive a string as input, potentially a mixture of upper and lower case, numbers, special characters etc. The task is to determine if the string contains at least one of each letter of the alphabet. Return true if all are found and false if not. Write it as a RESTful web service (no authentication necessary) in any language/framework you choose and document the service. Please bring your laptop on the day of your interview to present your information*
# Set up
This project uses `pipenv` for its dependancy and enviornment management

First install `pipenv` with `brew` or `pip`

Then install dependancies with:

`pipenv install`

Finally run the project using:

`pipenv run python main.py`


# Documentation
Swagger docs can be found here: http://localhost:5000/apidocs/#/default

This assignment was done using python 3 and flask-restful

Class Assignment1 contains a straight forward implementation using subsets:

http://127.0.0.1:5000/v1/contains-all-alphas/subset?string=myStringToCheck

Class Assignment2 uses set comprehension:

http://127.0.0.1:5000/v1/contains-all-alphas/loop?string=myStringToCheck
