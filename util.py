import directx_keycodes as dx_keys
import configparser
import os
import webbrowser

import re

from pynput import keyboard


def open_help():
	webbrowser.open("https://github.com/nickmarch96/ModularMacro", new=2)


def establish_keyboard_hook(hotkeys):
	with keyboard.GlobalHotKeys(hotkeys) as h:
		h.join()


def validate_macro(macro):
	if type(macro) != configparser.SectionProxy:
		print("validate_macro::Macro not of expected type! Skipping...")
		return False

	ret = dict()

	ret["macro_name"] = macro.get("macro_name", macro.name).strip()
	ret["description"] = macro.get("description", "").strip()
	ret["base_delay"] = macro.get("base_delay", "0.1").strip()
	ret["toggle"] = macro.get("toggle", "False").strip()

	for key in ["hotkey", "macro"]:
		if key not in macro.keys():
			print("validate_macro:::Macro '{}' missing parameter '{}'".format(ret["macro_name"], key))
			return False

	try:
		ret["base_delay"] = float(ret["base_delay"])
	except ValueError:
		print("validate_macro::Macro '{}' has invalid 'base_delay' of '{}'".format(ret["macro_name"], ret["base_delay"]))
		return False

	ret["hotkey"] = macro["hotkey"].strip().lower().split("+")

	for key in ret["hotkey"]:
		if key == "+":
			print("validate_macro::Macro '{}' has an unexpected '+' in hotkey".format(ret["macro_name"]))
			return False

		if len(key) > 1 and key not in dx_keys.PYNPUT_KEYCODES:
			print("validate_macro::Macro '{}' has unexpected sequence '{}' in hotkey".format(ret["macro_name"], key))
			return False

		if len(key) == 1 and key.upper() not in dx_keys.DIRECT_X_KEYCODES.keys():
			print("validate_macro::Macro '{}' has unexpected sequence '{}' in hotkey".format(ret["macro_name"], key))
			return False

		if key == "":
			print("validate_macro::Macro '{}' has an illformed hotkey".format(ret["macro_name"]))
			return False

	ret["hotkey"] = "+".join(ret["hotkey"])

	if ret["toggle"].upper() in ["TRUE", "T", "YES", "Y"]:
		ret["toggle"] = True
	elif ret["toggle"].upper() in ["FALSE", "F", "NO", "N"]:
		ret["toggle"] = False
	else:
		print("validate_macro::Macro '{}' has unexpected value '{}' for toggle.".format(ret["macro_name"], ret["toggle"]))
		return False

	macro["macro"] = macro["macro"].strip().replace(" ", "<SPACE>")
	macro_re = re.compile(r"[<][^>]+[>]")
	ret["macro"] = list()

	t = macro_re.search(macro["macro"])
	if not t:
		ret["macro"] = list(macro["macro"])

	else:
		while True:
			t = macro_re.search(macro["macro"])
			
			if not t:
				break

			for i in range(t.start()):
				ret["macro"].append(macro["macro"][i])
			ret["macro"].append(macro["macro"][t.start():t.end()])

			macro["macro"] = macro["macro"][t.end():]

		ret["macro"] = ret["macro"] + list(macro["macro"])

	return ret



def parse_config(path):
	config = configparser.ConfigParser()

	config.read(path)

	ret = dict(config)
	ret.pop("DEFAULT")

	if "MenuParams" not in ret.keys():
		print("parse_config::Missing MenuParams Section in Config!")
		return {}

	if "menu_name" not in ret["MenuParams"].keys():
		print("parse_config::Missing menu_name in MenuParams Section in Config!")
		return {}

	if "stop_key" not in ret["MenuParams"].keys():
		print("parse_config::Missing stop_key in MenuParams Section in Config!")
		return {}

	for key, value in ret.items():
		if key == "MenuParams":
			ret["MenuParams"] = dict(value)
		else:
			ret[key] = validate_macro(value)

	assert ret["MenuParams"]["menu_name"]

	return ret




