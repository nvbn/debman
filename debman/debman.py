#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from functools import partial
import sys, os
import json

__author__ = 'Vladimir Yakovlev'
__email__ = 'nvbn.rm@gmail.com'
__version__ = '0.1'


class DebmanPlugins:
    """Class for initialing debman plugins"""
    PLUGINS_DIR = '%s/.config/debman_plugins/' % os.getenv('HOME')
    DEFAULT = {
        'aptitude': (
            ('S', 'install', 'install package from repository'),
            ('Ss', 'search', 'search in repository'),
            ('Ssy', '%(app) update && %(app) search', 'update index and search'),
            ('Si', 'show', 'show package information'),
            ('Sr', 'install --without-recommends', 'install package from repository without recommends'),
            ('Sy', 'update', 'update package indexes'),
            ('Su', 'upgrade', 'update packages'),
            ('Suy', '%(app)s update && %(app)s upgrade', 'perform update and upgrade'),
            ('Qs', 'search %(val)s|egrep "^i"', 'search in installed packages'),
            ('Qc', 'changelog', 'show package changelog'),
            ('R', 'remove', 'remove package'),
            ('Rn', 'purge', 'purge package'),
            ('Sc', 'clean', 'clean cache'),
            ('Sw', 'download', 'download package without installation'),
        ),
        'apt-file': (
            ('Ql', 'list', 'list package content'),
            ('Qo', 'search', 'find package contains file'),
            ('Qy', 'update', 'update file in packages index'),
            ('Qly', '%(app)s update && %(app)s list', 'update files index and show content'),
            ('Qoy', '%(app)s update && %(app)s search', 'update files index and find package contains file'),
        ),
        'apt-get': (
            ('Sbd', 'build-dep', 'install build dependencies'),
        ),
        'dpkg': (
            ('U', '-i', 'install local package'),
        ),
        'apt-build': (
            ('Sb', 'install', 'build and install package from source'),
        ),
        'pip': (
            ('Sp', 'install', 'install package from pip'),
            ('Ssp', 'search', 'search package in pip'),
        )
    }

    def __init__(self, **kwargs):
        """Init class and override methods by kwargs"""
        for arg, val in kwargs.items():
            setattr(self, arg, val)
        self.plugins = dict()
        if os.path.isdir(self.PLUGINS_DIR):
            for plugin in os.listdir(self.PLUGINS_DIR):
                file = open(self.PLUGINS_DIR + plugin, 'r')
                self.plugins[plugin.split('_')[1]] = json.loads(file.read())
                file.close()
        else:
            os.mkdir(self.PLUGINS_DIR)
            for name, plugin in self.DEFAULT.items():
                file = open(self.PLUGINS_DIR + '00_' +  name, 'w')
                file.write(json.dumps(plugin))
                file.close()
            self.plugins = self.DEFAULT

    def __iter__(self):
        for plugin in self.plugins.items():
            yield plugin


class Debman:
    """Main debman class"""
    TREE = dict()
    HELP = ['  Usage: debman [opts] [args] \n',]

    def __init__(self, plugins, *args):
        """Create arguments tree and call function"""
        for name, actions in plugins:
            for action in actions:
                tpl = '%(param)s'
                if action[1].find('%(app)s') == -1:
                    tpl = "%(app)s " + tpl
                if action[1].find('%(val)s') == -1:
                    tpl += ' %%(val)s '
                else:
                    tpl = tpl.replace('%(val)s', '%%(val)s')
                self.TREE[action[0]] = tpl % {
                    'app': name,
                    'param': action[1],
                }
                self.HELP.append('  -%s -- %s' % (action[0], action[2],))
        if 'h' in args:
            self.__call__ = lambda param: sys.stdout.write('\n'.join(self.HELP) + '\n')
        else:
            self.__call__ = lambda param: os.system(self.TREE[''.join(sorted(''.join(args)))] % {
                'val': ' '.join(param)
            })

