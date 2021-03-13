# planner_app
This is a project I started over spring break 2021. It is a planner app geared towards students and is class/assignment oriented. I plan to continue working on this in the future. It uses the Django web framework. 

# Currentely it implements:

- User login, logout, and register
- individual dashboards for each User
- sql database
- Models for classes, assignments, and reminders
- Due dates for assignments with nice calendar picker functionality
- creating and deleting assingments, todos, and classes
- basic mobile responsitivity (dashboard)

I will be hosting it on Heroku soon for anyone to use. Feel free to use it if you like it but its kinda trash right now.

# Some features I will be implementing in the future:

- better mobile responsitivity for class view
- ability to edit things like class/assingment/reminder names, descriptions, due dates, etc.
- popups for creating classes, assingments, and reminders rather than different pages
- ordering assingments in a class in order of important and urgency
  (Each class has a due date and I will add an estimated time to complete. The longer and closer an assignment is, the more urgent it is therefore it will be at the    top of your list)
- Text message notifications for your reminder? Not sure whether there is an API or library to do this but if there is that would be really cool and helpful
- Global reminders on dash board along with being specific to each class
