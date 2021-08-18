#!/bin/sh

if [[! command -v python &> /dev/null ]]; then
    echo "Python could not be found..."
    echo "Installing python 3.9 ..."
    if [[ -x $(command -v yum) ]]; then
        sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel
        wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
        tar xzf Python-3.9.6.tgz
        cd Python-3.9.6
        sudo ./configure --enable-optimizations
        sudo make altinstall
        sudo rm Python-3.9.6.tgz
    elif [[ -x $(command -v apt-get) ]]; then
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt-get update
        sudo apt-get install python3.9
    elif [[ -x $(command -v pacman) ]]; then
        sudo pacman -S python
    else
        echo "Error can't install python 3.9"
        echo "Manually install it and then run os_handler.py"
        echo "Please open an issue at https://github.com/gbrunofranco/os-initializer so that I can add your OS to the list of supported ones!"
        exit 1;
    fi
fi

python os_handler.py