include .env

$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' .env))

build:
	docker run -v .:/src openapitools/openapi-generator-cli generate -g python -i /src/fdcnal-food-data_central_api-1.0.1-resolved.yaml -o /src/client