sudo sh ./dep.sh
sh ./dep_yay.sh
git clone https://github.com/dleyvacastro/Tests.git
cp -r ./Tests/kitty ~/.config
cp -r ./Tests/fish ~/.config
cd ~/.config
git clone https://github.com/dleyvacastro/qtile.git
git clone https://github.com/dleyvacastro/Neovim.git
mv Neovim nvim

