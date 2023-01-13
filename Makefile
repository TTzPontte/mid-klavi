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







dockerrun dkr:
	@ docker run -p 8000:8000 -d --rm --network lambda-local --name dynamodb -v $(CURDIR)/local/dynamodb:/data/ amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath /data

dockerstop dks:
	@ docker stop dynamodb

containerprune ctp:
	@ docker container prune

dockernetwork dkn:
	@ docker network create lambda-local

server:
	@ sam local start-api --docker-network lambda-local --parameter-overrides Table=Activities Region=us-east-1 AWSEnv=AWS_SAM_LOCAL

test:
	@ tox

package:
	@ python setup.py sdist
	@ echo "Your package is in the dist directory."

upload pypi:
	@ python setup.py sdist upload

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
