import PySimpleGUI as sg
import util
import os
import macro
import threading

sg.theme("Light Grey 1")

w_init = None
w_menu = None


def exit_menu():
	w_init.close()
	w_menu.close()


def gen_layout_init():
	title = sg.Text("Modular Macro Menu")

	fname = sg.Input(key="fname")
	fname_browse = sg.FileBrowse(file_types=(("config files","*.conf"),("all files","*.*")))
	fname_error = sg.Text(size=(30, 1), text_color="red", key="fname_error", visible=False)

	btn_load = sg.Button("Load Macros", key="btn_load")

	return [[title],
			[fname, fname_browse],
			[fname_error],
			[btn_load]]


def gen_layout_macro_single(macro, event_trigger):
	name = sg.Text(macro.name)
	hotkey = sg.Text("({})".format(macro.hotkey))
	status = sg.Text("Inactive", background_color="#841f27", key=macro.name + "status")
	desc = sg.Text(macro.description)

	macro.trigger = event_trigger

	layout = [[name, hotkey, status],
			[desc]]

	return [sg.Frame("", layout=layout, key=macro.name)]


def gen_layout_menu(config, macros):
	title = sg.Text(config["MenuParams"]["menu_name"])

	event_trigger = sg.Button("Click", key="event_trigger", metadata="")

	macro_frame = sg.Frame("Macros", layout = [gen_layout_macro_single(x, event_trigger) for x in macros], key="macro_frame")

	return [[title],
			[macro_frame],
			[event_trigger]]


def main():
	global w_init, w_menu

	w_init = sg.Window(title="Modular Macro Menu", layout=gen_layout_init())
	
	while True:
		event, val = w_init.Read()

		if event == sg.WIN_CLOSED or event == "Cancel":
			print("Quitting!")
			return

		elif event == "btn_load":
			w_init["fname_error"].Update(visible=False)

			if not val["fname"]:
				w_init["fname_error"].Update(value="No config selected.")
				w_init["fname_error"].Update(visible=True)

			else:

				try:
					config = util.parse_config(val["fname"])
					assert config
					break

				except:
					w_init["fname_error"].Update(value="{} was not loaded correctly.".format(os.path.basename(val["fname"])))
					w_init["fname_error"].Update(visible=True)


	menu_params = config.pop("MenuParams")

	hotkeys = {}

	loaded_macros = []

	for k, v in config.items():
		try:
			x = macro.Macro(**v)
			
			if x.hotkey not in hotkeys.keys():
				hotkeys[x.hotkey] = x.run_macro
				loaded_macros.append(x)

			else:
				print("Failed to load Macro '{}'. Reason: WARNING::Duplicate Hotkey {} found!".format(k, x.hotkey))

		except Exception as e:
			print("Failed to load Macro '{}'. Reason: {}".format(k, str(e)))

	config["MenuParams"] = menu_params

	w_menu = sg.Window(title="Modular Macro Menu", layout=gen_layout_menu(config, loaded_macros))

	t = threading.Thread(target=util.establish_keyboard_hook, args=(hotkeys,))
	t.daemon = True
	t.start()


	w_init.close()

	while True:
		event, val = w_menu.Read()

		if event == sg.WIN_CLOSED or event == "Cancel":
			print("Quitting!")
			return

		if event == "event_trigger":
			key = w_menu["event_trigger"].metadata
			try:
				status = key.split(":::")[-1]
				key = ":::".join(key.split(":::")[:-1])
				print(key, status)

				if status == "running":
					w_menu[key + "status"].Update(background_color="#0f6400")
					w_menu[key + "status"].Update(value="Active")
				else:
					w_menu[key + "status"].Update(background_color="#841f27")
					w_menu[key + "status"].Update(value="Inactive")

			except AttributeError as e:
				print(e)
				pass

		






main()



