# Yanne_tech
Task for Yanne Technology 24 Nov 2022

API to perform a CRUD operation of a Book Ledger

The API contains Admin page , Admin page Logger , API Logger , CORS header settings.

COR Origin settings can be changed in Yanne_tech/Settings.py 
Admin page Logger and API logger can be enabled or disabled in Yanne_tech/Global_config.py

---------------------TO RUN THE APPLICATION-----------------------------------
Step 1 ==> Create and Activate an Environment or Activate your existing Environment in the CMD/Terminal
Step 2 ==> Install libraries from requirements.txt in your Environment
Step 3 ==> Run the following command in your Environment
            python manage.py runserver 0.0.0.0:8000

NOTE : You can use the API URL in a Browser or any API client POSTMAN ,Testfully etc . This Django offers native UI to make API via any browser

The API provide three endpoints as mentioned below,
      1. BASE_URL/api/v1/bookledger/
      2. BASE_URL/api/v1/searchbyid/<int:book_id>/
      3. BASE_URL/api/v1/searchbygenre/<str:genre>/
      
 
 1 . /api/v1/bookledger/ -----------
 
      This Endpoint offers 2 methods POST and GET .
      POST Method to enter a new Book details in the Ledger 
      GET Method to View all the books in the Ledger
      
  2 . /api/v1/searchbyid/<int:book_id>/  ----------- Enter the required book id in the place of "<int:book_id>" in the URL
  
      This Endpoint offers 3 methods GET , PUT and DELETE
      GET Method to fetch the book details based on the given book_id
      PUT Method to change or update the details for the provided book_id
      DELETE Method to Delete the respective book_id
      
   3 . /api/v1/searchbygenre/<str:genre>/  ------------ Enter the required genre name in the place of "<str:genre>" in the URL
   
      This Endpoint offers 3 methods GET , PUT and DELETE
      GET Method to fetch the book details based on the given genre name 
      PUT Method to change or update the details for the provided genre name 
      DELETE Method to Delete the respective genre name 
