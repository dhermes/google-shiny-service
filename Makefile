GCLOUD_PROJECT:=$(shell gcloud config list project --format="value(core.project)")
GRPCIO_VIRTUALENV=$(shell pwd)/grpc_python_venv
PROTOC_CMD=$(GRPCIO_VIRTUALENV)/bin/python -m grpc.tools.protoc
GOOGLEAPIS_PROTOS_DIR=$(shell pwd)/googleapis-pb

help:
	@echo 'Makefile for Shiny service                                     '
	@echo '                                                               '
	@echo '   make generate-proto-files    Generates the protobuf modules.'
	@echo '   make docker-build    Builds the docker image.               '
	@echo '   make docker-push    Pushes the docker image.                '
	@echo '   make generate-container-engine-config    Generates the      '
	@echo '       Container Engine deployment configuration.              '
	@echo '   make deploy    Deploys the service to Container Engine.     '
	@echo '   make clean    Clean generated files.                        '

.PHONY: generate-proto-files
generate-proto-files:
	# Ensure we have a virtualenv
	[ -d $(GRPCIO_VIRTUALENV) ] || \
	    python -m virtualenv $(GRPCIO_VIRTUALENV)
	# Ensure virtualenv is up-to-date with grpcio/grpcio-tools
	$(GRPCIO_VIRTUALENV)/bin/pip install \
	    --upgrade grpcio grpcio-tools
	# Retrieve git repo with common *.proto files.
	[ -d $(GOOGLEAPIS_PROTOS_DIR) ] || git clone \
	    https://github.com/googleapis/googleapis \
	    $(GOOGLEAPIS_PROTOS_DIR) \
	    --depth=1
	# Need to install via "pip install --upgrade grpcio-tools"
	$(PROTOC_CMD) \
	    --proto_path=protos \
	    --proto_path=$(GOOGLEAPIS_PROTOS_DIR) \
	    --python_out=shiny \
	    --grpc_python_out=shiny \
	    protos/shiny.proto

.PHONY: docker-build
docker-build:
	docker build -t gcr.io/$(GCLOUD_PROJECT)/shiny .

.PHONY: docker-push
docker-push: docker-build
	gcloud docker push gcr.io/$(GCLOUD_PROJECT)/shiny

.PHONY: generate-container-engine-config
generate-container-engine-config:
	sed "s/\$$GCLOUD_PROJECT/$(GCLOUD_PROJECT)/g" container-engine.tmpl.yaml > container-engine.yaml

.PHONY: deploy
deploy: generate-container-engine-config docker-push
	kubectl create -f container-engine.yaml

.PHONY: clean
clean:
	rm -fr $(GRPCIO_VIRTUALENV) $(GOOGLEAPIS_PROTOS_DIR) container-engine.yaml
