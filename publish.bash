now="$(date +'%d/%m/%Y %Hh %mm %Ss')"

pelican -o deploy -s publishconf.py

git checkout -b gh-pages --track destiny/master

ghp-import deploy -b gh-pages -m "Publicado em $now" --cname=flavialopes.dev

git push git@github.com:FlaviaLopes/flavialopes.github.io.git gh-pages:master




