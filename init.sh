rm -R -f myfirstwiki&&
tiddlywiki myfirstwiki --init server &&
open http://127.0.0.1:8080/ &&
tiddlywiki myfirstwiki --listen
