import subprocess
import os


def install_docker():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(
        ["sudo", "apt", "install", "apt-transport-https", "ca-certificates", "curl", "software-properties-common"])

    get_gpg_key = subprocess.run(["curl", "-fsSL", "https://download.docker.com/linux/ubuntu/gpg"],
                                 stdout=subprocess.PIPE, check=True)
    add_gpg_key = subprocess.run(["sudo", "apt-key", "add", "-"], input=get_gpg_key.stdout, stdout=subprocess.PIPE,
                                 check=True)

    subprocess.run(
        ["sudo", "add-apt-repository", "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"])
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "docker-ce"])


def install_docker_compose():
    subprocess.run(["sudo", "apt", "install", "-y", "python3", "python3-pip"])
    subprocess.run(["sudo", "pip3", "install", "docker-compose"])


# Check if Docker is installed
def check_docker_version():
    try:
        docker_version_process = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        docker_compose_version_process = subprocess.run(["docker", "compose", "version"], capture_output=True,
                                                        text=True)

        # print(docker_version_process.returncode)
        # print(docker_compose_version_process.returncode)

        if docker_version_process.returncode == 0 and docker_compose_version_process.returncode == 0:
            print(f"Docker version installed is {docker_version_process.stdout} \n \n")
            print(f"Docker compose version installed on this machine is {docker_compose_version_process.stdout}\n \n")
        else:
            print("Docker not installed or unable to determine the version.\n \n")

    except FileNotFoundError:
        print("Docker and Docker compose are not installed. Initiating installation, please wait...\n \n")
        install_docker()
        install_docker_compose()
        print(f"Docker and Docker compose installation completed.\n \n")
        return False


check_docker_version()

# Use docker compose file to build containers
print("Using docker-compose.yml to bring up containers for Wordpress website\n \n")
result = subprocess.run(['docker', 'compose', '-f', 'docker-compose.yml', "up", "-d"], stderr=subprocess.PIPE)

if result.returncode == 0:
    running_containers = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
    print("These are the currently running containers:\n \n")
    print(running_containers.stdout)
    print("The wordpress website is ready now \n \n")

else:
    print("Command failed with error", result.stderr.decode())

# Prompt user for site name and edit /etc/hosts file
site_name = input("Enter the WordPress site name: \n \n")
mapping_exists = False

# Read and print the updated /etc/hosts file
with open('/etc/hosts', 'r+') as hostsfile:
    for line in hostsfile.readlines():
        if f"127.0.0.1  {site_name}" in line:
            print(f"Mapping for {site_name} already exists in /etc/hosts\n \n")
            mapping_exists = True
            break

    if not mapping_exists:
        hostsfile.seek(0, 2)
        hostsfile.write(f"127.0.0.1  {site_name}\n")
        hostsfile.seek(0)
        content = hostsfile.read()
        print("This is the edited /etc/hosts/ file with the new mapping appended\n \n")
        print(content)
print(f"Please open {site_name} in your browser")


# Delete containers and website
def website_deletion():
    delete_containers = input(
        "Once you are done setting up your Wordpress website, press D to bring down the website or Q to exit the script")
    if delete_containers == "D":
        try:
            deleted_containers = subprocess.run(["docker", "compose", "-f", "docker-compose.yml", "down"],
                                                capture_output=True, text=True, check=True)
            if deleted_containers.returncode == 0:
                print("The containers have been removed \n \n")
        except subprocess.CalledProcessError as e:
            print(f"Deletion of containers failed with error code {e}")

        if os.path.exists("./wordpress"):
            try:
                delete_website = subprocess.run(["rm", "-rf", "./wordpress"], capture_output=True, text=True,
                                                check=True)
                print(delete_website.stdout)
                print("The website data has been deleted\n \n")
            except subprocess.CalledProcessError as e:
                print(f"Deletion of website data failed with error code {e}")
        else:
            print("The 'wordpress' directory does not exist. No website data to delete.\n \n")

    elif delete_containers == 'Q':
        return 0

    elif delete_containers.lower():
        print("Please enter D to bring down the website \n \n")
        website_deletion()

    else:
        print("Please enter the requested input to delete the website and the containers\n \n")
        website_deletion()


website_deletion()
