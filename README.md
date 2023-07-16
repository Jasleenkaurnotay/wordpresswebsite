# YOUR WORDPRESS WEBSITE
## _Create your own wordpress website in LEMP stack_

'Your Wordpress Website' helps you create your own Wordpress website with a name of your choice. The website is built on a LEMP stack and employs the use of Docker containers. 

The code will first check if Docker and Docker Compose are installed on the machine. These services would be installed if not already present. Post that, a docker compose file would be used to bring up required containers - MySQL, Wordpress (with PHP) and nginx to create a Wordpress website. Users would be asked to input the name they would like to use for the website. Once the website is installed, the script offers the choice to either bring down the website (and the containers) or simply quit the script.

## Prerequisites:

- Linux (has been tested on Ubuntu 20.04)
- Python3 
- Docker, Docker compose

## Installation:

1. On the linux machine, check if python3 is installed:
   ```sh
   python3 --version
   ```

    If not installed, then you can install the latest version of python3 for your machine. For example, to install the latest version of Python3 on ubuntu 20.04, use the command:
    
    ```sh
    sudo apt update
    sudo apt install python3.8
    ```
## Usage

1. Clone this repository onto your linux machine by using its public URL
    ```sh
   git clone https://github.com/Jasleenkaurnotay/wordpresswebsite.git
   ```
2. Change into the cloned repository
    ```sh
   cd wordpresswebsite.git
   ```
3. At the terminal, inside the cloned directory execute the below command to run the script:
    ```sh
    sudo python3 main.py
    ```

## Expected Outcome:

1. Upon executing the script, if Docker and Docker Compose are installed on your machine, then you can expect to see their installed versions, similar to below:
    ```sh
    Docker version installed is Docker version 20.10.22, build 3a2c30b
    
    Docker compose version installed on this machine is Docker Compose version v2.15.1
    ```
    Docker and Docker compose aren't installed, then these services would be installed
2. The second stage would use the docker-compose.yml file to bring up containers of MySQL, Nginx and Wordpress(with PHP):

    ```sh
    Using docker-compose.yml to bring up containers for Wordpress website
    ```

3. If the containers are created successfully, an output of _"docker ps"_ command would be displayed on the screen, similar to the below:

    ```sh
    These are the currently running containers:
    CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS          PORTS                 NAMES
    bc6c32055d4b   nginx:latest                  "/docker-entrypoint.…"   37 seconds ago   Up 35 seconds   0.0.0.0:80->80/tcp    wordpresswebsite-nginx-1
    61e63be20c44   wordpress:php8.2-fpm-alpine   "docker-entrypoint.s…"   37 seconds ago   Up 35 seconds   9000/tcp              wordpresswebsite-wordpress-1
    dc8576a69fc9   mysql:latest                  "docker-entrypoint.s…"   37 seconds ago   Up 35 seconds   3306/tcp, 33060/tcp   wordpresswebsite-mysql-1
    ```
    Or else, in case of any errors, the respective error message would be displayed on the screen
4. Next, a prompt on the screen would indicate that the Wordpress website is ready:

    ```sh
    The wordpress website is ready now 
    ```

5. The user would be prompted to enter a name for this website:
    ```sh
    Enter the WordPress site name:
    ```
    
6. After an input is provided, a mapping for the provided name would be made in the /etc/hosts file to localhost. 
    ```sh
    Enter the WordPress site name:
    ```
    
    For repeated runs of the script, if the mapping is already present in /etc/hosts, then the prompt would indicate that. For example:
    ```sh
    Mapping for sample.com already exists in /etc/hosts
    ```

7. The script would prompt the user to now open the website with the provided name in a browser and wordpress website can then be configured to your liking:
    ```sh
    Please open sample.com in your browser
    ```

8. Once all work is done on the website, the user is presented with two options: to either leave the containers running and quit the script or to provide an input to delete the containers(and website data) and then finish running the script:

    ```sh
    Once you are done setting up your Wordpress website, press D to bring down the website or Q to exit the script
    ```
    
    If "D" is chosen then the containers and website related data would be removed from the machine. A prompt would confirm the deletion:
    ```sh
    The containers have been removed 
    The website data has been deleted
    ```


