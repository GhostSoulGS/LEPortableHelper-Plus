from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import xml.etree.ElementTree as ET
import os

# profiles = None
dp0 = os.path.dirname(__file__)
dp1 = f"{dp0}\Locale_Emulator"

def welcome_message():
	print("歡迎使用LEPortableHelper ,Locale Emulator便攜版")
	print("Welcome to LEPortableHelper, using Locale Emulator without install it.")

def profile_not_exist_message():
	print ('LEConfig.xml文件不存在,請按照')
	print ('')
# Locale_Emulator\LEConfig.xml
def load_xml():
	global profiles, LEProc
	LEProc = "Locale_Emulator\LEProc.exe"
	LEConfig = "Locale_Emulator\LEConfig.xml"
	profiles = ET.parse(LEConfig).getroot()[0]

def LE_1_button_start():
	global save_and_start
	save_and_start = True
	root.destroy()

def LE_2_button_start():
	global save_and_start
	save_and_start = False
	root.destroy()

def LE_3_3_button():
	global RuninJp_path
	LE_3_3 = tk.Tk() # 創建主窗口
	LE_3_3.withdraw() # 隱藏主窗口
	LE_3_3_path = filedialog.askdirectory(initialdir=RuninJp_path) # 使用目錄選擇對話框讓用戶選擇目錄
	LE_3_3.destroy() # 關閉主窗口
	if LE_3_3_path: # 判斷是否有輸入路徑
		print("save Path:", LE_3_3_path) # 顯示路徑
		RuninJp_path = LE_3_3_path # 覆蓋路徑

def LE_4_button_exit():
	exit()

def save_bat_start_file():
	global root,var3_1,var3_2
	root = tk.Tk()
	root.withdraw()
	var3_1 = tk.BooleanVar()
	var3_2 = tk.BooleanVar()

	LE_1 = tk.Toplevel(root)
	LE_1.geometry("149x70")
	LE_1.overrideredirect(True)
	LE_1.attributes("-topmost", 1)
	LE_1.configure(borderwidth=2)
	LE_1.configure(relief="raised")
	LE_1.configure(bg="#F0F8FF")

	LE_2 = tk.Toplevel(root)
	LE_2.geometry("149x70")
	LE_2.overrideredirect(True)
	LE_2.attributes("-topmost", 1)
	LE_2.configure(borderwidth=2)
	LE_2.configure(relief="raised")
	LE_2.configure(bg="#F0F8FF")

	LE_3 = tk.Toplevel(root)
	LE_3.geometry("347x29")
	LE_3.overrideredirect(True)
	LE_3.attributes("-topmost", 1)
	LE_3.configure(bg="#E7FEFF")

	LE_4 = tk.Toplevel(root)
	LE_4.geometry("185x26")
	LE_4.overrideredirect(True)
	LE_4.attributes("-topmost", 1)
	LE_4.configure(borderwidth=2)
	LE_4.configure(relief="raised")
	LE_4.configure(bg="#F0F8FF")

	LE_1_x = (LE_1.winfo_screenwidth() - LE_1.winfo_reqwidth()) / 2 - 100
	LE_1_y = (LE_1.winfo_screenheight() - LE_1.winfo_reqheight()) / 2 + 50

	LE_2_x = (LE_2.winfo_screenwidth() - LE_2.winfo_reqwidth()) / 2 + 100
	LE_2_y = (LE_2.winfo_screenheight() - LE_2.winfo_reqheight()) / 2 + 50

	LE_3_x = (LE_3.winfo_screenwidth() - LE_3.winfo_reqwidth()) / 2 - 100
	LE_3_y = (LE_3.winfo_screenheight() - LE_3.winfo_reqheight()) / 2 + 150

	LE_4_x = (LE_4.winfo_screenwidth() - LE_4.winfo_reqwidth()) / 2 - 16
	LE_4_y = (LE_4.winfo_screenheight() - LE_4.winfo_reqheight()) / 2 + 207

	LE_1.geometry("+%d+%d" % (LE_1_x, LE_1_y))
	LE_2.geometry("+%d+%d" % (LE_2_x, LE_2_y))
	LE_3.geometry("+%d+%d" % (LE_3_x, LE_3_y))
	LE_4.geometry("+%d+%d" % (LE_4_x, LE_4_y))

	LE_1_button = tk.Button(LE_1, text="Save to .bat", width=20, height=4, bg="#E7FEFF",highlightthickness=0, command=LE_1_button_start)
	LE_1_button.place(x=-1, y=-1)

	LE_2_button = tk.Button(LE_2, text="Run in Japanese", width=20, height=4, bg="#E7FEFF",highlightthickness=0, command=LE_2_button_start)
	LE_2_button.place(x=-1, y=-1)

	LE_3_checkbox_1 = tk.Checkbutton(LE_3, text="Admin(管理員)", width=0, height=0, bg="#E7FEFF", variable=var3_1, activebackground="#E7FEFF")
	LE_3_checkbox_1.place(x=2, y=2)

	LE_3_checkbox_2 = tk.Checkbutton(LE_3, text="RelativePath(相對路徑)", width=0, height=0, bg="#E7FEFF", variable=var3_2, activebackground="#E7FEFF")
	LE_3_checkbox_2.place(x=105, y=2)

	LE_3_button = tk.Button(LE_3, text="Path 自訂路徑", width=11, height=0, command=LE_3_3_button, bg="#E7FEFF")
	LE_3_button.place(x=258, y=2)

	LE_4_button = tk.Button(LE_4, text="[exit(關閉)]", width=25, height=0, command=LE_4_button_exit, bg="#E7FEFF")
	LE_4_button.place(x=-1, y=-1)

	root.mainloop()

def list_all_profiles(): # 選擇文件
	global RuninJp_name,RuninJp_path,RuninJp_LEProc,RuninJp_file
	RuninJp = tk.Tk() # 創建主窗口
	RuninJp.withdraw() # 隱藏主窗口
	RuninJp_file = filedialog.askopenfilename() # 使用文件選擇框選擇文件
	RuninJp.destroy() # 關閉主窗口
	assert RuninJp_file, "" # 判斷是否有輸入路徑
	print("\nstart path:", RuninJp_file)
	RuninJp_path, RuninJp_name = os.path.split(RuninJp_file) # 獲取目錄和檔名
	RuninJp_name,extension = os.path.splitext(RuninJp_name) # 去除副檔名
	RuninJp_LEProc = dp1

def RuninJp_Relative():
	global RuninJp_file,RuninJp_LEProc
	RuninJp_file = os.path.relpath(RuninJp_file, dp1) # 獲得目標相對路徑
	RuninJp_LEProc = os.path.relpath(dp1, RuninJp_path) # 獲得Locale_Emulator相對路徑

def LE_Admin_file():
	global profile_id
	if var3_1.get(): # 依管理員選擇抽取啟動參數
		selected_profile = profiles[1]
	else:
		selected_profile = profiles[0]
	profile_id = selected_profile.attrib['Guid']

def script_maker(): # 組成啟動路徑
	exe = "LEProc.exe -runas"
	return f"{exe} {profile_id} \"{RuninJp_file}\""

def save_to_file(cmd): # 創建bat
	new_name = f"{RuninJp_name}.bat"
	if os.path.exists(f"{RuninJp_path}\\{new_name}"):
			num = 0
			while True:
				new_name = f"{RuninJp_name}_{num}.bat"  # 创建新的文件名
				num += 1
				if not os.path.exists(f"{RuninJp_path}\\{new_name}"):  # 检查文件是否存在
					break

	with open(f"{RuninJp_path}\{new_name}", "w", encoding="utf-8") as f:
		f.write("chcp 65001 > nul\n")
		f.write("@echo off\n")
		f.write("cd \"" + RuninJp_LEProc + "\"\n")
		f.write("start \"\" " + cmd + "\n")
		f.write("exit\n\n\n\n")
		f.write(" .\    = 當前目錄\n")
		f.write(" ..\   = 上一個目錄\n")
		f.write(" ..\..\= 上上個目錄 (以此類推)\n\n\n")
		f.write(" cd 要填 bat 到 Locale_Emulator 的路徑\n\n")
		f.write(" 執行檔案位置要填 Locale_Emulator 到 目標檔案 的路徑\n\n")
		f.write(" start \"\" 能使CMD視窗不會等待目標程式關閉\n")

def run_now(): # 直接啟動
	print (f"\nstart {RuninJp_path}")
	os.system(f"{LEProc} -runas {profile_id} \"{RuninJp_file}\"")

if __name__ == '__main__':
	welcome_message()
	try:
		load_xml()
	except:
		profile_not_exist_message()
		input('Press [Enter] to exit.')
		exit()
	while(True):
		try:list_all_profiles();break
		except:exit()
	save_bat_start_file()
	LE_Admin_file()
	if save_and_start:
		if var3_2.get():
			RuninJp_Relative()
		cmd = script_maker()
		save_to_file(cmd)
	else:
		LE_Admin_file()
		run_now()