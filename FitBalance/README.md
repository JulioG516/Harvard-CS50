
# FitBalance

#### Video Demo: <https://youtu.be/sDKnM98f4is>

#### Description: Nutrition and Fitness WEB APP



#### Features used

* Python

* Flask

* HTML

* CSS

* Javascript



and an API to check for foods, which is the Edamam API.



## Project Explanation

My project it's a web based application, the goal was to make a fitness and nutritition app, that can deliver useful informations, like an calculator to body fat, to body mass index, how many macronutrients and calories a person needs, and how many calories and macronutrients do you have in each food by using an API to get the serch.


## Tools used and why
I used Flask to the back-end and handle the requests, but our main work was on JavaScript with calculations and formulas, i did not used Python and Flask to get the calculations, because we don't use any database on our server, its passed to the API and handled the JSONs with JavaScript.



## Each Page Description

#### Index.html

it's the apresentation part of my App, where the user can know more about the app.

#### bf.html

it's the body fat calculator, which uses Flask to get and deliver the request, and use JavaScript to make the calculation, i preferred to use front-end instead of back-end, because it's not a thing that i need to validate, isn't a crucial and security question to validate on the server-side.


#### BMI.html

it's the BMI (body mass index) Calculator that's uses process exactly like the BF calculator.

#### macro.html

calculate the macronutrient and calorie needs for a person, it use the process exactly like the BF, which is Flask handling with the GET method and delivering the page, with the front-end with JavaScript to make the calculation and validation of the site.

#### calories.html

Here is where we change some things, was made using an API provided by Edamam, and by the user input, we handle the JSONs, providing a page with a lot of foods and descriptions for them, how many carbohydrates ? how many proteins? and fats ? and was made using JavaScript too.

#### index.js
It's where sit's the main part of our code, here stay's the functions that store the variables and handle with each formula of our application, without this we can't get any calculations to work.

## Documentation

* https://flask.palletsprojects.com/en/1.1.x/

* https://developer.mozilla.org/en-US/docs/Web/JavaScript

* https://developer.mozilla.org/en-US/docs/Web/HTML
