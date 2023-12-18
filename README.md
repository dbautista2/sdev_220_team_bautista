# SDEV 220 Final Project 

Team Name: Bautista
Contributors:
1. Daniel Bautista (Lead)
2. Trey Auker
3. Christopher Brigham

## Description
The program name is Burger Smash.
It utilizes the Django framework to create a Point-of-sale webapp that allows the user to order a burger, sides, and a drink.
The user can choose from a variety of toppings, sides, and drinks. 

## Summary
Originally, we wanted to add Combos, multiple burgers per order, and show the grand total, but due to us running out of time, we had to take a step back and make the decision to leave some things out. 
Menu.html is the template used to show the data. Form.py is what allowed us to create the checkboxes for clicking specific items to add to the order. Models.py allowed us to store the information in a database. Views.py grabbed the data and passed it to the template. With our knowledge of Django, we thought we would be able to implement these in our project, but we just did not have enough time to get it all working. We created urls and other html files that we did not end up using, but it might be good to see our logic behind why we created them.
Created an ERD named my_project_visualized.png. It shows the relationships between everything involed in the program. 

## Django Usage
The following Django components are utilized to create the user driven POS (point of sale)
1. Admin - We utilize the Django admin to create the database tables for the toppings, sides, and drinks.
1. Models - We utilize the Django models to create the database tables for the toppings, sides, and drinks.
1. ModelForms - We utilize the Django ModelForms to create the forms for the user to select the toppings, sides, and drinks.
1. FormViews - We utilize the Django FormViews to create the views for the user to select the toppings, sides, and drinks.
1. Templates - We utilize the Django templates to create the HTML pages for the user to select the toppings, sides, and drinks.

### Running the application

1. Clone the repository
2. Navigate to the directory where the manage.py file is located
3. Run the following command to build the database, load seed data and start the server
```
python manage.py migrate
python manage.py loaddata fixtures/seed_data.json
python manage.py runserver
```

## Admin Login
Open a browser and navigate to http://localhost:8000/admin

Use the following credientials to login
``` 
username: admin
password: 123456
```
You may now add Burgers, Buns, Patties, Toppings, Sides, and Drinks these models are used to seed the data of the application.
You can cannot add Combos or Orders as they are for record keeping purposes.
Refund capabilities do not exist in the application.
## Customer Experience
Open a browser and navigate to http://localhost:8000/burgorders/welcome/

## Dumping data
You can configure your menu by editing the Burger, Bun, Patty, Topping, Side, and Drink models in the admin page.
Once you are happy with you menu you can dump the data to a json file by running the following command
``` 
python manage.py dumpdata --indent 4 --natural-foreign --natural-primary --exclude auth.permission --exclude contenttypes > fixtures/seed_data.json
```
