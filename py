	yum groupinstall "development tools" -y
	yum install epel-release -y 
	yum install -y libffi-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel 
	cd /usr/src/
	wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
	tar xzvf Python-3.8.2.tgz
	cd Python-3.8.2
	./configure --enable-optimizations
	make altinstall

