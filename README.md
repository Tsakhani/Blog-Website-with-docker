# Blog-Website-with-docker

1. Install Dependencies

Make sure the following dependencies are installed on your system:

    Docker: Install from Docker's official website.
    Docker Compose: Install from Docker Compose documentation.
    Git: Install Git from Git's official website.

2. Clone the Repository

Clone the project repository from GitHub:

git clone https://github.com/your-username/your-blog-repo.git
cd your-blog-repo

3. Build and Start the Services

Use Docker Compose to build the images and start the services:

docker-compose up -d

        Builds the Flask app image.
        Starts the Flask and Redis containers in detached mode.

4. Access the Website

Once the containers are running, open your browser and go to:

http://localhost:5000

5. Stop the Services

To stop the containers without removing them, run:

docker-compose stop

To stop and remove the containers, run:

docker-compose down

