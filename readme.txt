
Creating a Macro
Creating a macro can be broken down into a few steps.
	1. Define your macro section
		This is done with a new line and a [$NAME$]
	2. Define all parameters
		macro_name *optional 
		description *optional 
		hotkey
		base_delay * optional 
		toggle *optional 
		macro
	3. Run the program
		Upon running the program, you will be asked to select your macro config


========================
Creating a macro section
========================
	This is a unique section identifier for your macro. It must be unique
	from all other sections and will be used to keep track of your macro.
	
	Please keep in mind that a macro section name should consist of only
	uppercase and lowercase lettes. No symbols or spaces. This can cause
	unexpected crashes.
	
	Example:
		[MyNewMacro]

==================
Setting macro_name
==================
	This is the display name of the macro. This value is optional and
	not including it will default it to the Macro Section name.
	
	This can include any symbols, spaces, and new lines. This value will
	be displayed in the menu for ease of use.

	Example:
		macro_name = Cool Macro

===================
Setting description
===================
	This is a display description for the macro. This value is optional
	and not including it will default it to nothing.
	
	Can include symbols, spaces, and new lines. This value will be displayed
	in the help section of the menu

	Example:
		description = This macro lets me automate tasks on my computer.

==============
Setting hotkey
==============
	This will be the sequence of keys to press to activate the macro. If 
	toggle is enabled then this hotkey will also deactivate the macro.
	There is a limit by hardware that prevents more than 3 keys being presed
	at once. This means this is an invalid macro <CTRL>+<ALT>+<SHIFT>+T.
	
	Hotkeys can not contain symbols that require a command character to access
	such as '#' or '@'. If you want the hotkey to be a '#' then the hotkey
	would be <SHIFT>+3. Not <SHIFT>+#.
	
	When creating a hotkey the plus symbol is used to combine keys. Because
	of this, you can NOT have a '+' symbol as part of the sequence. Every
	key must be separated by a '+'. 
	
	*NOTE* If your hotkey is a single character and that character is
		in the macro. The hotkey will activate during the macro (causing a 
		self activating or deactivating macro)
	
	Example:
		A 			- valid
		A+T+P		- valid
		<CTRL>+h	- valid
		<SHIFT>++	- not valid
		<SHIFT>+<+>	- not valid

	Hotkeys that use special characters must be defined between braces.
	The complete list of special characters for hotkeys can be found below
	under the section 'HotKeys Special Characters'

	Example:
		hotkey = <CTRL>+1

==================
Setting base_delay
==================
	This is the delay in miliseconds for keypresses. Specifically, the time in
	in seconds between pressing a key down and releasing it. The lower the number
	the faster the macro will type. There is a balance as going too quickly
	will cause certain keys to be missed. From experiance, a pretty hard
	minimum is 0.005.
	
	If this parameter is missing, it will default to 0.1.

	Example:
		base_delay = 0.01

==============
Setting toggle
==============
	This parameter changes the behavior of the macro activation.
	By default the macro will execute whenever the hotkey is pressed.
	Setting this to true makes the macro repeat indefinitely when
	activated until the hotkey is pressed again. 
	
	If this parameter is missing, it will default to False.
	
	Example:
		toggle = True
	
=============
Setting macro
=============
	This is the meat of the macro definition. Macros are injected into
	the system using direct x. This means that direct x keycodes must be
	used. It is impractical to put in a sequence of hex codes so a
	translation table was made. Because of this, macro definitions must be
	made in a particular format.
	
	For alphanumeric (uppercase, lowercase, and numbers) enter the sequence
	as a string. Uppercase characters are automatically handled by pressing
	the right shift <SHIFT_R> key.

	Example:
		macro = 123abc
	
	For special characters keep in mind that direct x does not recognize 
	symbols, but rather keys. For example the '@' symbol is not an input
	for direct x. In order to press this key you must press <SHIFT> then
	press '2'. Macros can not interpret the values on the keys only the keys
	themselves. To define a key press as the <SHIFT> version of the key put
	the key in braces and prepend a '+'.
	
	Example:
		example<+2>email.com		- example@email.com
		Hello<SPACE>World<+1>		- Hello World!
		<+'>Semicolon;Colon<+;><+'>	- "Semicolon;Colon:"
	
	Lastly, ALL valid directx key codes are defined below in the section
	'DirectX KeyCodes'. All command keys (not alphanumeric or symbols) 
	must have braces (<__>) around it.
	*Note Spaces will be automatically handled by a ' ' character but can
		still be defined directly using <SPACE>*

	Example:
		<SHIFT_R><SPACE><F5><TAB><ESC>
		
	You can also insert delays into the macro directly. These delays are
	inserted inbetween the two keys and are added to the overall base delay.
	The syntax for inserting a delay is <DELAY=x>. Ensure there is no space
	within the delay control character. Otherwise, it will make a malformed
	Macro.
	
	Example:
		Hello<SPACE><DELAY=1>World<+1>
	
	
	

==========================
HotKeys Special Characters
==========================
	<alt>
	<alt_l>
	<alt_r>
	<backspace>
	<caps_lock>
	<ctrl>
	<ctrl_l>
	<ctrl_r>
	<delete>
	<up>
	<down>
	<left>
	<right>
	<enter>
	<esc>
	<shift>
	<shift_r>
	<space>
	<tab>
	<f1>
	<f2>
	<f3>
	<f4>
	<f5>
	<f6>
	<f7>
	<f8>
	<f9>
	<f10>
	<f11>
	<f12>
	<f13>
	<f14>
	<f15>
	<f16>
	<f17>
	<f18>
	<f19>
	<f20>
	<home>
	<end>
	<insert>
	<scroll_lock>
	<num_lock>
	<page_down>
	<page_up>
	<print_screen>
	<media_next>
	<media_play_pause>
	<media_previous>
	<media_volume_down>
	<media_volume_mute>
	<media_volume_up>
	<menu>
	<pause>

================
DirectX KeyCodes
================
 Available Direct X Key		  Hex Value
	"ESC":						0x01,
	"1":						0x02,
	"2":						0x03,
	"3":						0x04,
	"4":						0x05,
	"5":						0x06,
	"6":						0x07,
	"7":						0x08,
	"8":						0x09,
	"9":						0x0a,
	"0":						0x0b,
	"-":						0x0c,
	"=":						0x0d,
	"BACKSPACE":				0x0e,
	"TAB":						0x0f,
	"Q":						0x10,
	"W":						0x11,
	"E":						0x12,
	"R":						0x13,
	"T":						0x14,
	"Y":						0x15,
	"U":						0x16,
	"I":						0x17,
	"O":						0x18,
	"P":						0x19,
	"[":						0x1a,
	"]":						0x1b,
	"ENTER":					0x1c,
	"CTRL_L":					0x1d,
	"A":						0x1e,
	"S":						0x1f,
	"D":						0x20,
	"F":						0x21,
	"G":						0x22,
	"H":						0x23,
	"J":						0x24,
	"K":						0x25,
	"L":						0x26,
	";":						0x27,
	"'":						0x28,
	"`":						0x29,
	"SHIFT_L":					0x2a,
	"\\":						0x2b,
	"Z":						0x2c,
	"X":						0x2d,
	"C":						0x2e,
	"V":						0x2f,
	"B":						0x30,
	"N":						0x31,
	"M":						0x32,
	",":						0x33,
	".":						0x34,
	"/":						0x35,
	"SHIFT_R":					0x36,
	"DIK_MULTIPLY":				0x37,
	"ALT_L":					0x38,
	"SPACE":					0x39,
	"CAPS_LOCK":				0x3a,
	"F1":						0x3b,
	"F2":						0x3c,
	"F3":						0x3d,
	"F4":						0x3e,
	"F5":						0x3f,
	"F6":						0x40,
	"F7":						0x41,
	"F8":						0x42,
	"F9":						0x43,
	"F10":						0x44,
	"NUM_LOCK":					0x45,
	"SCROLL_LOCK":				0x46,
	"NUM7":						0x47,
	"NUM8":						0x48,
	"NUM9":						0x49,
	"DIK_SUBTRACT":				0x4a,
	"NUM4":						0x4b,
	"NUM5":						0x4c,
	"NUM6":						0x4d,
	"DIK_ADD":					0x4e,
	"NUM1":						0x4f,
	"NUM2":						0x50,
	"NUM3":						0x51,
	"NUM0":						0x52,
	"DIK_DECIMAL":				0x53,
	"F11":						0x57,
	"F12":						0x58,
	"F13":						0x64,
	"F14":						0x65,
	"F15":						0x66,
	"DIK_NUMPADEQUALS":			0x8d,
	"DIK_AT":					0x91,
	"DIK_COLON":				0x92,
	"DIK_UNDERLINE":			0x93,
	"DIK_STOP":					0x95,
	"DIK_UNLABELED":			0x97,
	"DIK_NUMPADENTER":			0x9c,
	"CTRL_R":					0x9d,
	"DIK_NUMPADCOMMA":			0xb3,
	"DIK_DIVIDE":				0xb5,
	"DIK_SYSRQ":				0xb7,
	"ALT_R":					0xb8,
	"HOME":						0xc7,
	"UP":						0xc8,
	"PAGEUP":					0xc9,
	"LEFT":						0xcb,
	"RIGHT":					0xcd,
	"END":						0xcf,
	"DOWN":						0xd0,
	"PAGEDOWN":					0xd1,
	"INSERT":					0xd2,
	"DELETE":					0xd3


