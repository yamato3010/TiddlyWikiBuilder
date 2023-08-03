mkdir ./myfirstwiki/plugins&&
cp -R ./sitemap ./myfirstwiki/plugins/&&
cd myfirstwiki&&
tiddlywiki --rendertiddlers '[!is[system]]' $:/core/templates/static.tiddler.html static text/plain&&
tiddlywiki --rendertiddler $:/core/templates/static.template.css static/static.css text/plain&&
tiddlywiki --rendertiddler sitemap sitemap.xml text/plain&&
cd ..&&
python3 decodeFilename.py&&
python3 decodeHTMLlink.py
