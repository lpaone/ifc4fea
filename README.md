ifc4fea
=======
Making FEA using BIM.

Prerequisiti
------------
1. Istallare il gestore completo di pacchetti per python 2.7.* [ANACONDA](https://www.anaconda.com/) scegliendo la versione appropriata per il SO in uso di  
2. Istallare [pythonocc-core](http://www.pythonocc.org/) usando da terminale ```$ conda install -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core==0.18.1```
3. Istallare [ifcopenshell-python](http://ifcopenshell.org/python.html) per il SO in uso


Git Recipies
------------

Clonare un repositorio di github.com
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

```
Controllare lo stato del repositorio
```
$ git status
```
Rimuovere dei files inutili anche se si è fatto .gitignore. La regola non funziona in modo retroattivo.
```
$ git rm --cached <files>
```
Per pubblicare sul repositorio remoto
```
git push https://github.com/lpaone/ifc4fea.git
```
Per aggiungere un file o una directory nuova
```
git add <file_name/dir_name>
```
