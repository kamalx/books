## Make new index.html

.PHONY: help html

html:
	@echo "Building new index..."
	@echo "Using " `which python`
	@echo `python --version`
	python render.py

help: 
	@echo "To build new index.html, use:"
	@echo "\$ python render.py"
