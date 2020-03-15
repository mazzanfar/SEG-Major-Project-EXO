install:
	echo 'installing nodejs'
	git clone https://github.com/nodejs/node
	cd node; \
	./configure \
	make; \
	sudo make install
