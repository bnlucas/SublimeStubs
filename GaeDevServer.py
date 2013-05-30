# Small Sublime Text 2 window command to start the GAE dev server from
# folder. Called from Side Menu context option.
#
# On my local setup, my app directories are stored directly under the GAE directory.
# C:\google_appengine\myapp
#
# Side Bar.sublime-menu file:
# [
# 	{ "caption": "-" },
# 	{
# 		"caption": "Start GAE Dev Server",
# 		"command": "gae_dev_server", "args": { "paths": [] }
# 	}
# ]

import sublime, sublime_plugin
import os

from threading import Thread

class GaeDevServerCommand(sublime_plugin.WindowCommand):

	def run(self, paths=[]):
		path = 'C:\\google_appengine\\' # change to GAE SDK directory.

		if os.path.dirname(paths[0]) == path:
			app    = paths[0].replace(''.join([path, os.sep]), '')
			server = 'python dev_appserver.py --clear_datastore=yes {app}/'
			cmd    = 'cd {path} && {server}'.format(path=path, server=server)

			Thread(target=os.system, args=[cmd.format(app=app)]).start()
