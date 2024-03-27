.PHONY: build-rust run-webserver build

build-rust:
	cd write_csv && \
	cargo build --release && \
	cd .. && \
	cp write_csv/target/release/write_csv tutorial/bin

run-webserver:
	source env/bin/activate && \
	cd tutorial && \
	dagster dev

build:
	$(MAKE) build-rust && \
	$(MAKE) run-webserver
