import ctypes
from time import sleep


DIRECT_X_KEYCODES = {
	"ESC": 0x01,
	"1": 0x02,
	"2": 0x03,
	"3": 0x04,
	"4": 0x05,
	"5": 0x06,
	"6": 0x07,
	"7": 0x08,
	"8": 0x09,
	"9": 0x0a,
	"0": 0x0b,
	"-": 0x0c,
	"=": 0x0d,
	"BACKSPACE": 0x0e,
	"TAB": 0x0f,
	"Q": 0x10,
	"W": 0x11,
	"E": 0x12,
	"R": 0x13,
	"T": 0x14,
	"Y": 0x15,
	"U": 0x16,
	"I": 0x17,
	"O": 0x18,
	"P": 0x19,
	"[": 0x1a,
	"]": 0x1b,
	"ENTER": 0x1c,
	"CTRL_L": 0x1d,
	"A": 0x1e,
	"S": 0x1f,
	"D": 0x20,
	"F": 0x21,
	"G": 0x22,
	"H": 0x23,
	"J": 0x24,
	"K": 0x25,
	"L": 0x26,
	";": 0x27,
	"'": 0x28,
	"`": 0x29,
	"SHIFT_L": 0x2a,
	"\\": 0x2b,
	"Z": 0x2c,
	"X": 0x2d,
	"C": 0x2e,
	"V": 0x2f,
	"B": 0x30,
	"N": 0x31,
	"M": 0x32,
	",": 0x33,
	".": 0x34,
	"/": 0x35,
	"SHIFT_R": 0x36,
	"DIK_MULTIPLY": 0x37,
	"ALT_L": 0x38,
	"SPACE": 0x39,
	"CAPS_LOCK": 0x3a,
	"F1": 0x3b,
	"F2": 0x3c,
	"F3": 0x3d,
	"F4": 0x3e,
	"F5": 0x3f,
	"F6": 0x40,
	"F7": 0x41,
	"F8": 0x42,
	"F9": 0x43,
	"F10": 0x44,
	"NUM_LOCK": 0x45,
	"SCROLL_LOCK": 0x46,
	"NUM7": 0x47,
	"NUM8": 0x48,
	"NUM9": 0x49,
	"DIK_SUBTRACT": 0x4a,
	"NUM4": 0x4b,
	"NUM5": 0x4c,
	"NUM6": 0x4d,
	"DIK_ADD": 0x4e,
	"NUM1": 0x4f,
	"NUM2": 0x50,
	"NUM3": 0x51,
	"NUM0": 0x52,
	"DIK_DECIMAL": 0x53,
	"F11": 0x57,
	"F12": 0x58,
	"F13": 0x64,
	"F14": 0x65,
	"F15": 0x66,
	"DIK_NUMPADEQUALS": 0x8d,
	"DIK_AT": 0x91,
	"DIK_COLON": 0x92,
	"DIK_UNDERLINE": 0x93,
	"DIK_STOP": 0x95,
	"DIK_UNLABELED": 0x97,
	"DIK_NUMPADENTER": 0x9c,
	"CTRL_R": 0x9d,
	"DIK_NUMPADCOMMA": 0xb3,
	"DIK_DIVIDE": 0xb5,
	"DIK_SYSRQ": 0xb7,
	"ALT_R": 0xb8,
	"HOME": 0xc7,
	"UP": 0xc8,
	"PAGEUP": 0xc9,
	"LEFT": 0xcb,
	"RIGHT": 0xcd,
	"END": 0xcf,
	"DOWN": 0xd0,
	"PAGEDOWN": 0xd1,
	"INSERT": 0xd2,
	"DELETE": 0xd3
}

PYNPUT_KEYCODES = [
	"<alt>",
	"<alt_l>",
	"<alt_r>",
	"<backspace>",
	"<caps_lock>",
	"<ctrl>",
	"<ctrl_l>",
	"<ctrl_r>",
	"<delete>",
	"<down>",
	"<end>",
	"<enter>",
	"<esc>",
	"<f1>",
	"<f10>",
	"<f11>",
	"<f12>",
	"<f13>",
	"<f14>",
	"<f15>",
	"<f16>",
	"<f17>",
	"<f18>",
	"<f19>",
	"<f2>",
	"<f20>",
	"<f3>",
	"<f4>",
	"<f5>",
	"<f6>",
	"<f7>",
	"<f8>",
	"<f9>",
	"<home>",
	"<insert>",
	"<left>",
	"<media_next>",
	"<media_play_pause>",
	"<media_previous>",
	"<media_volume_down>",
	"<media_volume_mute>",
	"<media_volume_up>",
	"<menu>",
	"<num_lock>",
	"<page_down>",
	"<page_up>",
	"<pause>",
	"<print_screen>",
	"<right>",
	"<scroll_lock>",
	"<shift>",
	"<shift_r>",
	"<space>",
	"<tab>",
	"<up>"
]

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
	_fields_ = [("wVk", ctypes.c_ushort),
				("wScan", ctypes.c_ushort),
				("dwFlags", ctypes.c_ulong),
				("time", ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
	_fields_ = [("uMsg", ctypes.c_ulong),
				("wParamL", ctypes.c_short),
				("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
	_fields_ = [("dx", ctypes.c_long),
				("dy", ctypes.c_long),
				("mouseData", ctypes.c_ulong),
				("dwFlags", ctypes.c_ulong),
				("time",ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
	_fields_ = [("ki", KeyBdInput),
				("mi", MouseInput),
				("hi", HardwareInput)]

class Input(ctypes.Structure):
	_fields_ = [("type", ctypes.c_ulong),
				("ii", Input_I)]

def PressKeyHex(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKeyHex(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def PressKeyBase(hexKeyCode, delay):
	PressKeyHex(hexKeyCode)
	sleep(delay)
	ReleaseKeyHex(hexKeyCode)

def PressShiftKeyBase(hexKeyCode, delay):
	shift = DIRECT_X_KEYCODES["SHIFT_R"]
	PressKeyHex(shift)
	PressKeyHex(hexKeyCode)
	sleep(delay)
	ReleaseKeyHex(hexKeyCode)
	ReleaseKeyHex(shift)


def PressKey(key, delay):
	if not key:
		return

	if len(key) == 1: # Then it is a character
		if key.isalnum(): # Then it is a letter
			c = DIRECT_X_KEYCODES[key.upper()]
			if key.isupper(): # then it is an uppercase letter. Shift must be pressed
				PressShiftKeyBase(c, delay)
			else:
				PressKeyBase(c, delay)
		elif key in DIRECT_X_KEYCODES.keys():
			c = DIRECT_X_KEYCODES[key.upper()]
			PressKeyBase(c, delay)
		else:
			print("PressKey::Invalid character '{}' in macro!".format(key))

	elif key[0] == "<" and key[-1] == ">": # Its a control character
		key = key[1:-1]

		if key[0] == "+" and key[1:].upper() in DIRECT_X_KEYCODES.keys():  # Its a shifted character
			c = DIRECT_X_KEYCODES[key[1:].upper()]
			PressShiftKeyBase(c, delay)

		elif key.split("=")[0].upper() == "DELAY": # It is a delay
			c = key.split("=")[-1]

			try:
				x = float(c)
				sleep(x)
			except ValueError:
				print("PressKey::Invalid delay '{}' in macro!".format(key))

		elif key.upper() in DIRECT_X_KEYCODES.keys():
			c = DIRECT_X_KEYCODES[key.upper()]
			PressKeyBase(c, delay)

		else:
			print("PressKey::Invalid Key '{}' in macro!".format(key))

	elif key.upper() in DIRECT_X_KEYCODES.keys():
		c = DIRECT_X_KEYCODES[key.upper()]
		PressKeyBase(c, delay)

	else:
		print("PressKey::Invalid Key '{}' in macro!".format(key))

