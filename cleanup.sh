sudo cp -r ./dotfiles/etc/X11/xorg.conf.d/00-keyboard.conf /etc/X11/xorg.conf.d/
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si