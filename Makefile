## Make new index.html

.PHONY: help html

help: 
	@echo "    -----------------------------"
	@echo "    To build new index.html, use:"
	@echo "        $ make html"
	@echo "    -----------------------------"

html:
	@echo "Building new index..."
	@echo "Using " `which python`
	@echo `python --version`
	python render.py
