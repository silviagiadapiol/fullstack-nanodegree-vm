## TABLE OF CONTENTS

* The program
* What's included
* Quick Start
* License


### THE PROGRAM
tournament.py is a Python file with a set of functions that allows the user to populate, clear and query the tournament database (defined in tournament.sql file). The tournament follows the "swiss tournament" rules for matching players.


### WHAT'S INCLUDED

In Silvia Giada Piol GitHub fullstack-nanodegree-vm repository, inside vagrant/[tournament, ](https://github.com/silviagiadapiol/fullstack-nanodegree-vm/tree/master/vagrant/tournament)  you can find the following files:
* tournament.sql _(it creates the swiss tournament database and its tables and view as sql statements)_
* tournament.py _(it gives the definitions of the functions that allows the user to interact with the tournament database)_
* db.py _(it gives the definitions of the class that allows to connect to the database, to execute querys, to commit and to close the connection)_
* tournament_test.py _(it tests all the functions defined in tournament. py)_


### QUICK START. 

Fork the repository and clone it on local machine. 
To test the program functionality run the test program from the virtual machine terminal 

`vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py`



### LICENSE

Creator Silvia Giada Piol, this code is released under the [MIT LICENCE](http://choosealicense.com/licenses/mit/)