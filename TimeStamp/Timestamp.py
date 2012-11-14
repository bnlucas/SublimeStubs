import datetime
import sublime, sublime_plugin

class TimestampCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		sels = self.view.sel()
		for sel in sels:
			self.view.erase(edit, sel)
			self.view.insert(edit, sel.begin(), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))