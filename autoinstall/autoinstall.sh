echo "----Autoinstall----"
echo "Welcome to the autoinstall process"
echo "Installing necesary aplications"

sudo sh ./dep.sh
yay -S nerd-fonts-ubuntu-mono
yay -S nerd-fonts-victor-mono

echo "---Another software---"
echo "install software by pacman? [1/0]"
read sp
if [ $sp == 1 ]
then
    sudo sh ./def.sh
fi

echo "Install software by yay? [1/0]"
if [ $sy == 1 ]
then
    sh ./dep_yay.sh
fi

echo "Install custom config? (kitty, rofi, fish, neovim, qtile) [1/0]"
read cc
if [ $cc == 1 ]
then

    git clone https://github.com/dleyvacastro/Tests.git
    cp -r ./Tests/kitty ~/.config
    cp -r ./Tests/fish ~/.config
    cp -r ./Tests/rofi ~/.config
    cd ~/.config
    git clone https://github.com/dleyvacastro/qtile.git
    git clone https://github.com/dleyvacastro/Neovim.git
    mv Neovim nvim
fi

