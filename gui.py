import PySimpleGUI as sg
import util
import os
import sys
import macro
import threading


sg.theme("Light Grey 1")

LIGHT_BLUE = "#0079d3"
LIGHT_GRAY = "#dae0e6"
WHITE = "#ffffff"
RED = "#d3000f"
GREEN ="#0f6400"
BLACK = "#1a1a1b"


w_init = None
w_menu = None


def exit_menu():
	w_init.close()
	w_menu.close()


def gen_layout_init():
	title = sg.Text("Modular Macro Menu", font=("Helvetica", 15, "bold"), justification="center", size=(31,1))

	ask = sg.Text("Please select a macro config.", font=("Helvetica", 10))

	fname = sg.Input(key="fname")
	fname_browse = sg.FileBrowse(file_types=(("config files","*.conf"),("all files","*.*")))
	fname_error = sg.Text(size=(30, 1), text_color="red", key="fname_error", visible=False)

	btn_load = sg.Button("Load Macros", key="btn_load")

	return [[title],
			[ask],
			[fname, fname_browse],
			[fname_error],
			[btn_load]]


def gen_layout_macro_single(macro, event_trigger):
	name = sg.Text(macro.name,
		text_color = WHITE,
		background_color = LIGHT_BLUE,
		font = ("Helvetica", 12, "bold"),
		key = macro.name + ":::name",
		enable_events = True
		)

	vs = sg.VerticalSeparator(color = LIGHT_BLUE,
		key = macro.name + ":::vs"
		)

	status = sg.Text("Inactive",
		text_color = WHITE,
		background_color = RED,
		font = ("Helvetica", 10, "bold"),
		key = macro.name + ":::status",
		enable_events = True
		)

	hotkey = sg.Text(f"({macro.hotkey})",
		text_color = WHITE,
		background_color = LIGHT_BLUE,
		key = macro.name + ":::hotkey",
		visible = False,
		enable_events = True
		)

	desc = sg.Text(macro.description,
		text_color = WHITE,
		background_color = LIGHT_BLUE,
		key = macro.name + ":::desc",
		visible = False,
		enable_events = True,
		metadata = False
		)	

	macro.trigger = event_trigger

	layout = [[name, vs, status],
			[hotkey],
			[desc]]

	frame = sg.Frame("",
		layout = layout, 
		background_color = LIGHT_BLUE,
		relief = "sunken",
		key = macro.name + ":::frame"
		)

	return [frame]


def gen_layout_menu(config, macros):

	menu_def = [["File", ["Go Back", "Exit"]],
				["Tools", ["Toggle Freeze"]],
				["Help", ["Open Docs"]]]

	menu = sg.Menu(menu_def,
		background_color=None,
		size=(None, None),
		tearoff=False,
		font=None,
		pad=None,
		key=None,
		k=None,
		visible=True,
		metadata=None)

	title = sg.Text(config["MenuParams"]["menu_name"],
		font = ("Helvetica", 15, "bold"),
		justification = "center",
		key = "menu_title"
		)

	event_trigger = sg.Button("Click",
		key = "event_trigger",
		metadata = "",
		visible = False
		)

	macro_frame = sg.Frame("Macros",
		layout = [gen_layout_macro_single(x, event_trigger) for x in macros],
		font = ("Helvetica", 10, "bold"),
		relief = "solid",
		border_width = 0,
		key = "macro_frame"
		)

	return [[menu],
			[title],
			[macro_frame],
			[event_trigger]]


def main():
	global w_init, w_menu

	w_init = sg.Window(title="Modular Macro Menu", layout=gen_layout_init())
	
	while True:
		event, val = w_init.Read()

		if event == sg.WIN_CLOSED or event == "Cancel":
			return 0

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

	w_menu = sg.Window(title="Modular Macro Menu", layout=gen_layout_menu(config, loaded_macros), text_justification="center", element_justification="center")

	t = threading.Thread(target=util.establish_keyboard_hook, args=(hotkeys,))
	t.daemon = True
	t.start()


	w_init.close()

	while True:
		event, val = w_menu.Read()

		if event == sg.WIN_CLOSED or event == "Cancel":
			return 0

		elif event == "event_trigger":
			macro_name = w_menu["event_trigger"].metadata
			try:
				status = macro_name.split(":::")[-1]
				macro_name = ":::".join(macro_name.split(":::")[:-1])

				if status == "running":
					w_menu[macro_name + ":::status"].Update(background_color=GREEN)
					w_menu[macro_name + ":::status"].Update(value="Active")
				else:
					w_menu[macro_name + ":::status"].Update(background_color=RED)
					w_menu[macro_name + ":::status"].Update(value="Inactive")

			except AttributeError as e:
				print(e)
				pass

		elif event == "Exit":
			return 0

		elif event == "Go Back":
			return -1

		elif event == "Open Docs":
			util.open_help()

		elif event == "Toggle Freeze":
			macro._FROZEN = not macro._FROZEN

			if macro._FROZEN:
				w_menu["menu_title"].Update(value = "FROZEN")
				w_menu["menu_title"].Update(text_color = LIGHT_BLUE)

			else:
				w_menu["menu_title"].Update(value = config["MenuParams"]["menu_name"])
				w_menu["menu_title"].Update(text_color = BLACK)


		else:
			elem = event.split(":::")[-1]
			macro_name = ":::".join(event.split(":::")[:-1])

			if elem and macro_name:
				if elem in ["name", "status", "hotkey", "desc", "vs"]:

					w_menu[macro_name + ":::hotkey"].Update(visible=True)
					w_menu[macro_name + ":::desc"].Update(visible=True)

					cur_state = w_menu[macro_name + ":::desc"].metadata

					if cur_state:
						w_menu[macro_name + ":::hotkey"].hide_row()
						w_menu[macro_name + ":::desc"].hide_row()
					else:
						w_menu[macro_name + ":::hotkey"].unhide_row()
						w_menu[macro_name + ":::desc"].unhide_row()

					cur_state = not cur_state
					w_menu[macro_name + ":::desc"].metadata = cur_state




		

if __name__ == "__main__":
	if main() == -1:
		try:
			os.execv(__file__, sys.argv)
		except OSError:
			try:
				os.execv(sys.executable, ['python'] + sys.argv)
			except:
				pass



