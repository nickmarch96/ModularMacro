import directx_keycodes as dx_keys
import threading

_FROZEN = False

class Macro:
	def __init__(self, macro_name, description, macro, base_delay, hotkey, toggle=False, trigger=None):
		self.name = macro_name
		self.description = description
		self.macro = macro
		self.delay = base_delay
		self.__toggle_en = toggle
		self.__toggle = toggle
		self.running = False

		self.hotkey = hotkey

		self.trigger = trigger

		self.__interrupt = False

	def __str__(self):
		return "Macro: {} ({})\n".format(self
			.name, self.hotkey) +\
			"\t{}\n".format(self.description)

	def __run_macro(self):
		if self.trigger:
			self.trigger.metadata = self.name + ":::running"
			self.trigger.Click()

		self.__interrupt = False

		while True:
			for key in self.macro:
				dx_keys.PressKey(key, self.delay)

				if self.__interrupt:
					break


			if not self.__toggle:
				break

		self.running = False

		if self.trigger:
			self.trigger.metadata = self.name + ":::stopped"
			self.trigger.Click()

	def run_macro(self):
		if _FROZEN:
			return

		if self.running:
			self.__interrupt = True

			if self.__toggle_en:
				self.__toggle = False

		else:
			if self.__toggle_en:
				self.__toggle = True

			t = threading.Thread(target=self.__run_macro)
			t.daemon = True
			t.start()
			self.running = True





