all: example hello

example:
	@echo Building example...
	./example_build.py
	@echo Running example...
	./example_main.py

hello:
	@echo Building hello...
	./hello_build.py
	@echo Running hello...
	./hello_main.py

clean:
	rm -f *.{c,o,so}
