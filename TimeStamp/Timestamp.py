import datetime
import sublime, sublime_plugin

class TimestampCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		sels = self.view.sel()
		for sel in sels:
			self.view.erase(edit, sel)
			self.view.insert(edit, sel.begin(), timestamp)