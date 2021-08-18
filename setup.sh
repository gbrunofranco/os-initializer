#!/bin/sh
git clone https://github.com/gbrunofranco/dotfiles.git
sudo cp -r ./dotfiles/etc/X11/xorg.conf.d/00-keyboard.conf /etc/X11/xorg.conf.d/