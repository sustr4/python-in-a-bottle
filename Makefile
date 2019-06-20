all:
	cd my-app && ng build && cd ..

run:
	flask run --host=0.0.0.0
