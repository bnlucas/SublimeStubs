# Small Sublime Text 2 window command to start the GAE dev server from
# folder. Called from Side Menu context option.

import sublime, sublime_plugin

import os

from threading import Thread

path = 'C:\\nathan\\appengine'

class GaeDevServerCommand(sublime_plugin.WindowCommand):

	def run(self, paths=[]):

		if os.path.dirname(paths[0]) == path:
			app    = paths[0].replace(''.join([path, os.sep]), '')
			server = 'python dev_appserver.py --clear_datastore=yes {app}/'
			cmd    = 'cd {path} && {server}'.format(path=path, server=server)

			Thread(target=os.system, args=[cmd.format(app=app)]).start()
