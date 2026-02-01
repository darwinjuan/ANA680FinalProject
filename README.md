Hello, this repository contains the files for the ANA680 Final Project Assignment which involves training the model to predict the occurence of heart disease based on the top four features using the heart disease dataset (heart disease.csv), developing a Flask application from it, deploying to Heroku, creating a Dockerfile, containerizing the model and pushing to Docker Hub, as well as redoing the project on AWS EC2 using project image along with nginx image. Please let me know if you have any questions. Thanks!
The objective of this project is to build a machine learning model that can predict the presence of heart disease in patients based on four different medical variables.
This model is predicting whether heart disease is likely based off the features: ST_Slope, Exercise Angina, Oldpeak, and Chest Pain Type. The features were chosen based off the high correlation between the features and the target variable (Heart Disease).
I used the Random Forest Classifier algorithm to predict the presence of heart disease and used that to build out a Flask application. I then deployed it to Heroku and also containerized and pushed it to Docker Hub. I then added it to AWS EC2 so that it is being hosted on there.

The process for running the application locally with Docker is as follows:
1) Pull image from Docker Hub using: docker pull darwinjuan/heart-disease-app:v1
2) Run the container: docker run -p 5000:5000 darwinjuan/heart-disease-app:v1
3) Access the app: http://localhost:5000

The process to deploy the containerized application to AWS EC2 is as follows:
1) Log into the AWS EC2 console and launch the t3.micro instance using Amazon Linux 2023
2) Create and download a key pair
3) Edit security rules to allow for inbound traffic
4) Connect the instance via SSH: ssh -i "aws-key.pem" ec2-user@ec2-54-177-48-248.us-west-1.compute.amazonaws.com

You would then install Docker on the server, create a nginx.conf file, create a docker-compose.yml file, then start the application through: docker-compose up -d. This will allow you to view and use the application when you enter the AWS Public IP address into your browser.
