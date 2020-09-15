# ModularMacro

ModularMacro is a Windows tool that leverages DirectX to bind hotkeys to keyboard sequences. Since the macros are DirectX keys, they work inside of all Windows applications and more importantly games. 

### Installation

ModularMacro is compiled with `auto-py-to-exe` and a json file of its configuration can be found within the resources folder. The required python libraries can be found within requirements.txt. You can run this as either an executable or a script from command line. 

If you don't want to have to worry about compiling or having python, a working executable can be found in the dist folder.

### Creating Macros

Creating a macro can be broken down into a few steps.
1. Define your macro section
    * This is done with a new line and a [NAME]
2. Define all parameters
   * macro_name *optional 
   * description *optional 
   * hotkey
   * base_delay * optional 
   * toggle *optional 
   * macro
3. Run the program
    * Upon running the program, you will be asked to select your macro config

### Creating a Macro Section

This is a unique section identifier for your macro. It must be unique from all other sections and will be used to keep track of your macro.

Please keep in mind that a macro section name should consist of only uppercase and lowercase lettes. No symbols or spaces. This can cause unexpected crashes.

macro.conf
```
[MyNewMacro]
    macro_name = My Macro
    description = A description
        Can even have new lines
    hotkey = <CTRL>+<ALT>+7
    base_delay = 0.01
    toggle = False
    macro = I can type out sentences very quick.
```

### Macro Parameters
macro_name:
This is the display name of the macro. This value is optional and not including it will default it to the Macro Section name.
This can include any symbols, spaces, and new lines. This value will be displayed in the menu for ease of use.
```
macro_name = Cool Macro
```
---
description:
This is a display description for the macro. This value is optional and not including it will default it to nothing.
Can include symbols, spaces, and new lines. This value will be displayed in the help section of the menu.
```
description = This macro does such as such.
    I use it to automate tasks on my computer!
```
---
hotkey:
This will be the sequence of keys to press to activate the macro. If  toggle is enabled then this hotkey will also deactivate the macro. There is a limit by hardware that prevents more than 3 keys being presed at once. This means this is an invalid macro <CTRL>+<ALT>+<SHIFT>+T.
Hotkeys can not contain symbols that require a command character to access such as '#' or '@'. If you want the hotkey to be a '#' then the hotkey would be <SHIFT>+3. Not <SHIFT>+#.
When creating a hotkey the plus symbol is used to combine keys. Because of this, you can NOT have a '+' symbol as part of the sequence. Every key must be separated by a '+'. 

*NOTE* If your hotkey is a single character and that character is in the macro. The hotkey will activate during the macro (causing a self activating or deactivating macro)
```
hotkey = A 			    - valid
hotkey = A+T+P		    - valid
hotkey = <CTRL>+h	    - valid
hotkey = <SHIFT>++	    - not valid
hotkey = <SHIFT>+<+>	- not valid
```
Hotkeys that use special characters must be defined between braces. The complete list of special characters for hotkeys can be found below under the section 'HotKeys Special Characters'
```
hotkey = <CTRL>+1
```
---
base_delay:
This is the delay in miliseconds for keypresses. Specifically, the time in seconds between pressing a key down and releasing it. The lower the number the faster the macro will type. There is a balance as going too quickly will cause certain keys to be missed. From experiance, a pretty hard minimum is 0.005.
	
If this parameter is missing, it will default to 0.1.
```
base_delay = 0.05
```
---
toggle:
This parameter changes the behavior of the macro activation. By default the macro will execute whenever the hotkey is pressed. Setting this to true makes the macro repeat indefinitely when activated until the hotkey is pressed again. 

If this parameter is missing, it will default to False.
```
toggle = True       OR      toggle = False
```
Valid values of this parameter are [TRUE, T, YES, Y, FALSE, F, NO, N]

---
macro:
This is the meat of the macro definition. Macros are injected into the system using direct x. This means that direct x keycodes must be used.
It is impractical to put in a sequence of hex codes so a translation table was made. Because of this, macro definitions must be made in a particular format.

For alphanumeric (uppercase, lowercase, and numbers) enter the sequenceas a string.
Uppercase characters are automatically handled by pressing the right shift <SHIFT_R> key.
```
macro = ABC123abc
```

For special characters keep in mind that direct x does not recognize symbols, but rather keys. For example the '@' symbol is not an inputfor direct x.
In order to press this key you must press <SHIFT> then press '2'. Macros can not interpret the values on the keys only the keys themselves.
To define a key press as the <SHIFT> version of the key put the key in braces and prepend a '+'.
```
macro = example<+2>email.com		- example@email.com
macro = Hello<SPACE>World<+1>		- Hello World!
macro = <+'>Semicolon;Colon<+;><+'>	- "Semicolon;Colon:"
```

Lastly, ALL valid directx key codes are defined below in the section 'DirectX KeyCodes'.
All command keys (not alphanumeric or symbols) must have braces (<__>) around it.

*Note Spaces will be automatically handled by a space character but can still be defined directly using <SPACE>*
```
macro = <SHIFT_R><SPACE><F5><TAB><ESC>
```

You can also insert delays into the macro directly. These delays are inserted inbetween the two keys and are added to the overall base delay.
The syntax for inserting a delay is <DELAY=x> where x is seconds.
Ensure there is no space within the delay control character. Otherwise, it will make a malformed Macro.
```
macro = Hello<SPACE><DELAY=1.5>World<+1>
```

### HotKeys Special Characters
```
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
```

### DirectX KeyCodes
```
ESC
1
2
3
4
5
6
7
8
9
0
-
=
BACKSPACE
TAB
Q
W
E
R
T
Y
U
I
O
P
[
]
ENTER
CTRL_L
A
S
D
F
G
H
J
K
L
;
'
`
SHIFT_L
\
Z
X
C
V
B
N
M
,
.
/
SHIFT_R
DIK_MULTIPLY
ALT_L
SPACE
CAPS_LOCK
F1
F2
F3
F4
F5
F6
F7
F8
F9
F10
NUM_LOCK
SCROLL_LOCK
NUM7
NUM8
NUM9
DIK_SUBTRACT
NUM4
NUM5
NUM6
DIK_ADD
NUM1
NUM2
NUM3
NUM0
DIK_DECIMAL
F11
F12
F13
F14
F15
DIK_NUMPADEQUALS
DIK_AT
DIK_COLON
DIK_UNDERLINE
DIK_STOP
DIK_UNLABELED
DIK_NUMPADENTER
CTRL_R
DIK_NUMPADCOMMA
DIK_DIVIDE
DIK_SYSRQ
ALT_R
HOME
UP
PAGEUP
LEFT
RIGHT
END
DOWN
PAGEDOWN
INSERT
DELETE
```





