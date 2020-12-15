# DjangoProject
#You can use the prepared virtual environment in venv folder for running the project 
#Handling Requests for a user app in a website with Django RestframeWork

#User app
URL -->  /user/login
POST:Login
required data:
-username
-password


/user/signup
POST:Signup
required data:
-username
-password
-first_name
-last_name
-email


/user/profile
PUT: edit profile
required data:
-first_name
-last_name


/user/list 
GET: get users list