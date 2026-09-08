.PHONY: generate check

generate:
	python3 internal/generate_readme.py
	prettier --write README.md dictionary/*.md internal/*.md > /dev/null

check:
	python3 internal/generate_readme.py --check

page:
	cd internal && python3 build_page.py
