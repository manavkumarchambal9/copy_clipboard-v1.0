#imports
import pyautogui
import win32clipboard
from pynput import keyboard
import os
from distutils.dir_util import copy_tree
from shutil import copy

#keyboard.ctrl_l=1
#__builtins__

copied_items=[]

def copy_path():
	pyautogui.keyDown('shift')
	pyautogui.rightClick()
	pyautogui.keyUp('shift')
	try:
		pyautogui.click(pyautogui.locateCenterOnScreen("Screenshot (8).png"))
	except:
		try:
			pyautogui.click(pyautogui.locateCenterOnScreen("Screenshot (9).png"))
		except:
			try:
				pyautogui.click(pyautogui.locateCenterOnScreen("Screenshot (6).png"))
			except:
				pyautogui.click(pyautogui.locateCenterOnScreen("Screenshot (7).png"))

	#pyautogui.press('down',presses=16)
	#pyautogui.press('enter')

def set_clipboard_data_none():
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText('')
	win32clipboard.CloseClipboard()

def set_clipboard_data(x):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(x)
	win32clipboard.CloseClipboard()

def get_clipboard_data():
	os.system('CLS')
	global copied_items
	win32clipboard.OpenClipboard()
	try:
		data=win32clipboard.GetClipboardData()
		if data not in copied_items and data!='':
			copied_items.insert(0,data)
			for i in range(len(copied_items)):
				print(i+1,' .' ,copied_items[i])			
		if len(copied_items)==10:
			copied_items.pop()
		#if data in copied_items:
			#x=X.index(data)
			#print(x)
			#copied_items.insert(0, copied_items.pop(x))
	except:
	    pass
	win32clipboard.CloseClipboard()

def main1():
	copy_path()
	try:
		get_clipboard_data()
	except:
		pass
	#print(copied_items)
	set_clipboard_data_none()

def main2():
	try:
		get_clipboard_data()
	except:
		pass
	#print(copied_items)
	set_clipboard_data_none()

def copy_folder(source, destination):
	new_folder=os.path.basename(source)
	os.chdir(destination)
	os.mkdir(new_folder)
	new_destination=os.path.join(destination, new_folder)
	copy_tree(source, new_destination)

def copy_file(source, destination):
	copy(source, destination)

def file_handeler(folder):
	try:
		pyautogui.hotkey('ctrl','l')
		pyautogui.hotkey('ctrl','c')
		win32clipboard.OpenClipboard()
		dest=win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		set_clipboard_data_none()
		folder=folder.replace('"','')
		if os.path.isdir(folder):
			copy_folder(folder,dest)
		if os.path.isfile(folder):
			copy_file(folder, dest)
	except:
		pass
	#print('code not written yet...')
	#pass

def main3():
	global current, copied_items
	on_index=(copied_items[int(eval(str(current[-1])))-1])
	if os.path.exists((on_index).replace('"','')):
		file_handeler(on_index)
	else:
		set_clipboard_data(on_index)
		print()
		pyautogui.hotkey('ctrl', 'v')
		set_clipboard_data_none()

#print('pressed ctrl + v')

#__main__



current=[]

combinations1=[[keyboard.Key.shift, keyboard.KeyCode(char='x')]]
combinations2=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='c')]]
combinations3=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=1)]]
combinations4=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=2)]]
combinations5=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=3)]]
combinations6=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=4)]]
combinations7=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=5)]]
combinations8=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=6)]]
combinations9=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=7)]]
combinations10=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=8)]]
combinations11=[[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v'), keyboard.KeyCode(char=9)]]
	
def on_press(key):
	global current, combinations1, combinations2, combinations3, combinations4, combinations5,combinations6, combinations7, combinations8, combinations9, combinations10, combinations11
	if key == keyboard.Key.esc:
		return False
	if any([key in COMBO for COMBO in combinations1]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==2:
				main1()
	elif any([key in COMBOs for COMBOs in combinations2]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==2:
				main2()
	elif any([key in COMBOss for COMBOss in combinations3]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOsss for COMBOsss in combinations4]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOssss for COMBOssss in combinations5]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOsssss for COMBOsssss in combinations6]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOssssss for COMBOssssss in combinations7]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOsssssss for COMBOsssssss in combinations8]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOssssssss for COMBOssssssss in combinations9]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOsssssssss for COMBOsssssssss in combinations10]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()
	elif any([key in COMBOssssssssss for COMBOssssssssss in combinations11]):
		if key not in current:
			current.append(key)
			#print(current)
			if len(current)==3:
				main3()

def on_release(key):
	global current, combinations1, combinations2
	if any([key in COMBO for COMBO in combinations1]) or any([key in COMBOs for COMBOs in combinations2]) or any([key in COMBOss for COMBOss in combinations3]) or any([key in COMBOsss for COMBOsss in combinations4]) or any([key in COMBOsssss for COMBOsssss in combinations6]) or any([key in COMBOssss for COMBOssss in combinations5]) or any([key in COMBOssssss for COMBOssssss in combinations7]) or any([key in COMBOsssssss for COMBOsssssss in combinations8]) or any([key in COMBOssssssss for COMBOssssssss in combinations9]) or any([key in COMBOsssssssss for COMBOsssssssss in combinations10]) or any([key in COMBOssssssssss for COMBOssssssssss in combinations11]) :
		current=[]	                
try:
	try:
		with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		 	listener.join()
	except:
		with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		 	listener.join()
except:
	pass
os.system('PAUSE')
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	 	listener.join()