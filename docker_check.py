import subprocess


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
docker_version_process = subprocess.run(["docker", "--version"], capture_output=True, text=True)
if docker_version_process.returncode != 0:
    print("Docker not installed. Initiating installation...")
    install_docker()
    print("Docker installation completed.")
else:
    print(f"Docker version installed is {docker_version_process.stdout}")

# Check if Docker Compose is installed
docker_compose_version_process = subprocess.run(["docker-compose", "--version"], capture_output=True, text=True)
if docker_compose_version_process.returncode != 0:
    print("Docker Compose not installed. Initiating installation...")
    install_docker_compose()
    print("Docker Compose installation completed.")
else:
    print(f"Docker compose version installed is {docker_compose_version_process.stdout}")
