echo Making sure we are using version control...
git init
echo Creating symlink to Ale
ln -s .ale/recipes_installed/ale/main.py ale
git add ale .ale .gitmodules
git commit -a -m 'Pouring some ale on it'