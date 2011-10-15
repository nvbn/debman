About
=====
debman - apt frontend with pacman syntax

debman can
==========

- -Ql -- list package content
- -Qo -- find package contains file
- -Qy -- update file in packages index
- -Qly -- update files index and show content
- -Qoy -- update files index and find package contains file
- -S -- install package from repository
- -Ss -- search in repository
- -Ssy -- update index and search
- -Si -- show package information
- -Sr -- install package from repository without recommends
- -Sy -- update package indexes
- -Su -- update packages
- -Suy -- perform update and upgrade
- -Qs -- search in installed packages
- -Qc -- show package changelog
- -R -- remove package
- -Rn -- purge package
- -Sc -- clean cache
- -Sw -- download package without installation
- -Sp -- install package from pip
- -Ssp -- search package in pip
- -Sbd -- install build dependencies
- -Sb -- build and install package from source
- -U -- install local package

Debman support plugins, yay!
============================

Plugins stored in ~/.config/debman_plugins/, plugin file name is NN_app (00_aptitude - low priority aptitude plugin).

Plugin is a json file with format:

[["Keys", "action", "description"], ["NewKeys?", "%(app)s action %(val)s", "description"]]

As example, for pip it's look: [["Sp", "install", "install package from pip"], ["Ssp", "search", "search package in pip"]]

