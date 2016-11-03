GRPCIO_VIRTUALENV=$(shell pwd)/grpc_python_venv
PROTOC_CMD=$(GRPCIO_VIRTUALENV)/bin/python -m grpc.tools.protoc
GOOGLEAPIS_PROTOS_DIR=$(shell pwd)/googleapis-pb

help:
	@echo 'Makefile for Shiny service                        '
	@echo '                                                  '
	@echo '   make generate    Generates the protobuf modules'
	@echo '   make clean       Clean generated files         '

generate:
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

clean:
	rm -fr $(GRPCIO_VIRTUALENV) $(GOOGLEAPIS_PROTOS_DIR)

.PHONY: generate clean
