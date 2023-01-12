# Variables
IMAGE_NAME = my-lambda-function
CONTAINER_NAME = my-lambda-function-container
DOCKERFILE = Dockerfile

# Default target
all: build

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) .

# Run the Docker container
run:
	docker run --name $(CONTAINER_NAME) -it $(IMAGE_NAME)

# Stop and remove the Docker container
clean:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true


test:
	python -m pytest tests/unit -v

start:
	sam local start-api
## Variables
#LAMBDA_NAME = my-lambda-function
#ZIP_FILE = function.zip
#
## Default target
#all: build
#
## Build the function
#build:
#	zip -r $(ZIP_FILE) .
#
## Deploy the function
#deploy:
#	aws lambda update-function-code --function-name $(LAMBDA_NAME) --zip-file fileb://$(ZIP_FILE)
#
## Invoke the function
#invoke:
#	aws lambda invoke --function-name $(LAMBDA_NAME) --log-type Tail --query 'LogResult' --output text output.txt | base64 --decode
#
## Clean up the build
#clean:
#	rm -f $(ZIP_FILE)
