from pynput import keyboard
import util
import directx_keycodes as dx_keys
import threading
from getpass import getpass
from time import sleep


_RUNNING = True

class Macro:
	def __init__(self, macro_name, description, macro, base_delay, hotkey, toggle=False):
		self.name = macro_name
		self.description = description
		self.macro = macro
		self.delay = base_delay
		self.__toggle_en = toggle
		self.__toggle = toggle
		self.running = False

		self.hotkey = hotkey

	def __str__(self):
		return "Macro: {} ({})\n".format(self
			.name, self.hotkey) +\
			"\t{}\n".format(self.description)

	def __run_macro(self):
		while True:
			for key in self.macro:
				dx_keys.PressKey(key, self.delay)

			if not self.__toggle:
				break

		self.running = False

	def run_macro(self):
		if not self.running:
			if self.__toggle_en:
				self.__toggle = True

			t = threading.Thread(target=self.__run_macro)
			t.daemon = True
			t.start()
			self.running = True

		elif self.__toggle_en:
			self.__toggle = not self.__toggle


def quit_menu():
	global _RUNNING
	_RUNNING = False


def establish_keyboard_hook(hotkeys):
	with keyboard.GlobalHotKeys(hotkeys) as h:
		h.join()	


def main():
	if not util.check_admin():
		print("Script not running as Administrator. Attempting to elevate...")
		print("Please do not close this window.")
		util.elevate()
		return


	util.os.system('cls')

	print("Please select the Macro config file to load macros.")

	fname = util.openfile()

	if not fname:
		print("No config file selected.\nQuitting...")
		sleep(2)
		return

	config = util.parse_config(fname)

	if config == {}:
		print("macro_menu::{} was not loaded correctly.".format(util.os.path.basename(fname)))
		print("Quitting...")
		sleep(2)
		return
	
	menu_params = config.pop("MenuParams")

	print("{} Started!".format(menu_params["menu_name"]))
	print("Press {} to stop the menu.\n".format(menu_params["stop_key"]))

	hotkeys = {
		menu_params["stop_key"]: quit_menu
	}

	loaded_macros = []

	for k, v in config.items():
		try:
			x = Macro(**v)
			
			if x.hotkey not in hotkeys.keys():
				hotkeys[x.hotkey] = x.run_macro
				loaded_macros.append(x)

			else:
				print("Failed to load Macro '{}'. Reason: WARNING::Duplicate Hotkey {} found!".format(k, x.hotkey))

		except Exception as e:
			print("Failed to load Macro '{}'. Reason: {}".format(k, str(e)))

	print("Number of Macros loaded: {}\n".format(len(loaded_macros)))
	print("Loaded Macros:")
	print("\n".join(["\t" + x.name for x in loaded_macros]))

	print("\nPress Enter to start the menu!")
	getpass(">:")

	util.os.system('cls')
	print("{}".format(menu_params["menu_name"]))
	print("Press {} to stop the menu.\n".format(menu_params["stop_key"]))
	print("\n".join(["({}) {}".format(i+1, str(loaded_macros[i])) for i in range(len(loaded_macros))]))
	
	t = threading.Thread(target=establish_keyboard_hook, args=(hotkeys,))
	t.daemon = True
	t.start()

	while _RUNNING:
		sleep(1)

	print("Quitting...")
	sleep(1)
	return


if __name__ == '__main__':
	main()

