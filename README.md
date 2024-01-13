# Parse url endpoints and HTTP methods from yaml and monitor their health

To run it:
- Build a Docker container: docker build -t {your_container_name} .
- Run the docker container: docker run -t {your_container_name} /app/config/config.yaml

to provide your yaml, either place the file in the /config dir and rebuild it, or run the docker with volumes (mount the local dir to use the local config file) like so:
- docker run -v /local/path/to/file.yaml:/container/path/to/your_file.yaml -t {your_container_name} /container/path/to/your_file.yaml

alternatively without docker:
- have python3 installed
- run: pip install -r requirements.txt 
- run the program with: python src/main.py /path/to/your/file.yaml

Ctrl + c to exit
