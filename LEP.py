import logging
import tarfile
from tkinter import filedialog
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
import xml.etree.ElementTree as ET
import shutil
import os

# profiles = None
dp0 = os.path.dirname(__file__)
LE_3_3_LEcopy = False

def welcome_message():
	print("歡迎使用LEPortableHelper ,Locale Emulator便攜版")
	print("Welcome to LEPortableHelper, using Locale Emulator without install it.")

def profile_not_exist_message():
	print ('LEConfig.xml文件不存在,請按照')
	print ('')
# Locale_Emulator\LEConfig.xml
def load_xml():
	global profiles, LEProc, menu_name, profile_id, LEP_
	LEP_ = "LEP\LEProc.exe"
	LEProc = "Locale_Emulator\LEProc.exe"
	LEConfig = "Locale_Emulator\LEConfig.xml"
	profiles = ET.parse(LEConfig).getroot()[0]
	menu_name = [profile.get("Name") for profile in profiles[:]] # 提取名稱
	profile_id = profiles[0].attrib['Guid'] # 默認設置

def LE_1_button_start(): # 判別正常運作
	global save_and_start
	try:
		if var3_1.get():
			if var3_2.get() and LE_3_3_LEcopy:
				os.path.relpath(LEcopy_path, RuninJp_path)
		else:
			if var3_2.get():
				os.path.relpath(f"{dp0}\{LEProc}", RuninJp_path)
		save_and_start = True
		root.destroy()
	except: # 顯示錯誤圖片
		LE_1_image.pack()
		LE_1.after(1500, lambda: LE_1_image.pack_forget())

def LE_2_button_start():
	global save_and_start
	save_and_start = False
	root.destroy()

def LE_3_3_button(): # 自定路徑
	global RuninJp_path, LEcopy_path, LE_3_3_LEcopy
	LE_3_3 = tk.Tk() # 創建主窗口
	LE_3_3.withdraw() # 隱藏主窗口
	LE_3_3.attributes("-topmost", True)  # 置頂
	LE_3_3_path = filedialog.askdirectory(initialdir=RuninJp_path, title="放置bat", parent=LE_3_3) # 使用目錄選擇對話框讓用戶選擇目錄
	if LE_3_3_path: # 判斷是否有輸入路徑
		print("save Path:", LE_3_3_path) # 顯示路徑
		RuninJp_path = LE_3_3_path # 覆蓋路徑
		if var3_1.get():
			LE_3_3_LEcopy_path = filedialog.askdirectory(initialdir=RuninJp_path, title="放置LE", parent=LE_3_3)
			print("copy Path:", LE_3_3_LEcopy_path) # 顯示路徑
			if LE_3_3_LEcopy_path: # 判斷是否有輸入路徑
				LEcopy_path = LE_3_3_LEcopy_path
				LE_3_3_LEcopy = True 
	LE_3_3.destroy() # 關閉主窗口

def LE_4_Guid_file(num):
	global profile_id
	profile_id = profiles[num].attrib['Guid']

def LE_5_button_exit():
	exit()

def open_PNG():
	global RelativePath_png, LEP_png
	with tarfile.open("PNG", 'r') as tar: # 讀取 tarball

		RelativePath_png = tar.extractfile('RelativePath.png').read() # 提取檔案的二進制數據
		RelativePath_png = Image.open(BytesIO(RelativePath_png)) # 將二進制數據轉換為 Pillow 圖像對象
		RelativePath_png = ImageTk.PhotoImage(RelativePath_png) # 將圖像轉換為 PhotoImage 對象，以便在 tk.Label 中顯示

		LEP_png = tar.extractfile('LEP.png').read() # 提取圖片的二進制數據
		LEP_png = Image.open(BytesIO(LEP_png)) # 將二進制數據轉換為 Pillow 圖像對象
		LEP_png = ImageTk.PhotoImage(LEP_png) # 將圖像轉換為 PhotoImage 對象，以便在 tk.Label 中顯示

def save_bat_start_file():
	global root,var3_1,var3_2,LE_1,LE_1_image
	root = tk.Tk()
	root.withdraw()
	var3_1 = tk.BooleanVar()
	var3_2 = tk.BooleanVar()

	open_PNG() # 提取圖片

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
	LE_4.geometry("266x30")
	LE_4.overrideredirect(True)
	LE_4.attributes("-topmost", 1)
	LE_4.configure(bg="#E7FEFF")

	LE_5 = tk.Toplevel(root)
	LE_5.geometry("185x26")
	LE_5.overrideredirect(True)
	LE_5.attributes("-topmost", 1)
	LE_5.configure(borderwidth=2)
	LE_5.configure(relief="raised")
	LE_5.configure(bg="#F0F8FF")

	LE_1_x = (LE_1.winfo_screenwidth() - LE_1.winfo_reqwidth()) / 2 - 100
	LE_1_y = (LE_1.winfo_screenheight() - LE_1.winfo_reqheight()) / 2 + 50

	LE_2_x = (LE_2.winfo_screenwidth() - LE_2.winfo_reqwidth()) / 2 + 100
	LE_2_y = (LE_2.winfo_screenheight() - LE_2.winfo_reqheight()) / 2 + 50

	LE_3_x = (LE_3.winfo_screenwidth() - LE_3.winfo_reqwidth()) / 2 - 100
	LE_3_y = (LE_3.winfo_screenheight() - LE_3.winfo_reqheight()) / 2 + 150

	LE_4_x = (LE_4.winfo_screenwidth() - LE_4.winfo_reqwidth()) / 2 - 58
	LE_4_y = (LE_4.winfo_screenheight() - LE_4.winfo_reqheight()) / 2 + 207

	LE_5_x = (LE_5.winfo_screenwidth() - LE_5.winfo_reqwidth()) / 2 - 16
	LE_5_y = (LE_5.winfo_screenheight() - LE_5.winfo_reqheight()) / 2 + 264

	LE_1.geometry("+%d+%d" % (LE_1_x, LE_1_y))
	LE_2.geometry("+%d+%d" % (LE_2_x, LE_2_y))
	LE_3.geometry("+%d+%d" % (LE_3_x, LE_3_y))
	LE_4.geometry("+%d+%d" % (LE_4_x, LE_4_y))
	LE_5.geometry("+%d+%d" % (LE_5_x, LE_5_y))

	LE_1_button = tk.Button(LE_1, text="Save to .bat", width=20, height=4, bg="#E7FEFF",highlightthickness=0, command=LE_1_button_start)
	LE_1_button.place(x=-1, y=-1)

	LE_1.image = RelativePath_png # 保留對 PhotoImage 對象的引用，以免被當垃圾回收
	LE_1_image = tk.Label(LE_1, image=RelativePath_png) # 創建 Label，顯示圖片
	LE_1_image.configure(relief="flat")
	LE_1_image.configure(bg="#E7FEFF")
	LE_1_image.place(x=0, y=0)
	LE_1_image.place_forget()

	LE_2_button = tk.Button(LE_2, text="Run it now", width=20, height=4, bg="#E7FEFF",highlightthickness=0, command=LE_2_button_start)
	LE_2_button.place(x=-1, y=-1)

	LE_3_checkbox_1 = tk.Checkbutton(LE_3, text="LEcopy(加LE)-", width=0, height=0, bg="#E7FEFF", variable=var3_1, activebackground="#E7FEFF")
	LE_3_checkbox_1.place(x=2, y=2)

	LE_3_checkbox_2 = tk.Checkbutton(LE_3, text="RelativePath(相對路徑)", width=0, height=0, bg="#E7FEFF", variable=var3_2, activebackground="#E7FEFF")
	LE_3_checkbox_2.place(x=105, y=2)

	LE_3_button = tk.Button(LE_3, text="Path 自訂路徑", width=11, height=0, command=LE_3_3_button, bg="#E7FEFF")
	LE_3_button.place(x=258, y=2)

	LE_4.image = LEP_png # 保留對 PhotoImage 對象的引用，以免被當垃圾回收
	LE_4_image = tk.Label(LE_4, image=LEP_png) # 創建 Label，顯示圖片
	LE_4_image.configure(relief="flat")
	LE_4_image.configure(bg="#E7FEFF")
	LE_4_image.place(x=0, y=-3)

	LE_4_menu = tk.StringVar(LE_4) # 創建下拉式菜單
	LE_4_menu.set(menu_name[0])  # 初始選項
	LE_4_menu_styles = tk.OptionMenu(LE_4, LE_4_menu, *menu_name, command=lambda x: LE_4_Guid_file(menu_name.index(LE_4_menu.get())))
	LE_4_menu_styles.config(width=27, height=0, bg="#FFFFFF", activebackground="#FFFFFF")
	LE_4_menu_styles["menu"].config(bg="#FFFFFF")
	LE_4_menu_styles.configure(relief="groove")
	LE_4_menu_styles.place(x=33, y=0)

	LE_5_button = tk.Button(LE_5, text="[exit(關閉)]", width=25, height=0, command=LE_5_button_exit, bg="#E7FEFF")
	LE_5_button.place(x=-1, y=-1)

	root.mainloop()


def list_all_profiles(): # 選擇文件
	global RuninJp_name,RuninJp_path,RuninJp_LEProc,RuninJp_file
	RuninJp = tk.Tk() # 創建主窗口
	RuninJp.withdraw() # 隱藏主窗口
	RuninJp_file = filedialog.askopenfilename(title="目標對象") # 使用文件選擇框選擇文件
	RuninJp.destroy() # 關閉主窗口
	assert RuninJp_file, "" # 判斷是否有輸入路徑
	print("\nstart path:", RuninJp_file)
	RuninJp_path, RuninJp_name = os.path.split(RuninJp_file) # 獲取目錄和檔名
	RuninJp_name,extension = os.path.splitext(RuninJp_name) # 去除副檔名
	RuninJp_LEProc = f"{dp0}\{LEProc}"

def LEcopy(): # 複製LE
	global LEcopy_path, RuninJp_LEProc, new_num
	if LE_3_3_LEcopy:
		if not os.path.exists(f"{LEcopy_path}\LEP"):  # 检查文件是否存在
			shutil.copytree(".\Locale_Emulator", f"{LEcopy_path}\LEP")
	else:
		if not os.path.exists(f"{RuninJp_path}\LEP"):  # 检查文件是否存在
			shutil.copytree(".\Locale_Emulator", f"{RuninJp_path}\LEP")
		LEcopy_path = RuninJp_path
	RuninJp_LEProc = f"{LEcopy_path}\{LEP_}"
	
def RuninJp_Relative(): # 獲得目標相對路徑
	global RuninJp_file,RuninJp_LEProc
	if var3_1.get():
		RuninJp_file = os.path.relpath(RuninJp_file, RuninJp_path) # 獲得目標相對路徑
		RuninJp_LEProc = os.path.relpath(f"{LEcopy_path}\{LEP_}", RuninJp_path) # 獲得Locale_Emulator相對路徑
	else:
		RuninJp_file = os.path.relpath(RuninJp_file, RuninJp_path) # 獲得目標相對路徑
		RuninJp_LEProc = os.path.relpath(f"{dp0}\{LEProc}", RuninJp_path) # 獲得Locale_Emulator相對路徑

def script_maker(batpath): # 組成啟動路徑
	exe = f"\"{RuninJp_LEProc}\" -runas"
	return f"{exe} {profile_id} \"{batpath}{RuninJp_file}\""

def save_to_file(cmd): # 創建bat
	new_name = f"{RuninJp_name}.bat"
	if os.path.exists(f"{RuninJp_path}\{new_name}"):
			num = 0
			while True:
				new_name = f"{RuninJp_name}_{num}.bat"  # 创建新的文件名
				num += 1
				if not os.path.exists(f"{RuninJp_path}\{new_name}"):  # 检查文件是否存在
					break

	with open(f"{RuninJp_path}\{new_name}", "w", encoding="utf-8") as f:
		f.write("chcp 65001 > nul\n")
		f.write("@echo off\n\n")
		f.write("start \"\" " + cmd + "\n\n")
		f.write("exit\n\n\n\n")
		f.write(" .\    = 當前目錄\n")
		f.write(" ..\   = 上一個目錄\n")
		f.write(" ..\..\= 上上個目錄 (以此類推)\n\n")
		f.write(" %~dp0 =  bat當前目錄\n\n")
		f.write(" start \"\" 能使CMD視窗不會等待目標程式關閉\n\n")

def run_now(): # 直接啟動
	print (f"\nstart {RuninJp_path}")
	os.system(f"{LEProc} -runas {profile_id} \"{RuninJp_file}\"")

if __name__ == '__main__':
	try:
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
		if save_and_start:
			if var3_1.get():
				LEcopy()
			if var3_2.get():
				RuninJp_Relative()
				cmd = script_maker("%~dp0")
			else:
				cmd = script_maker("")
			save_to_file(cmd)
		else:
			run_now()
	except Exception as e:
		logging.error(f"錯誤警報: {e}")
#		input()  # 如果有需要可以解放這行,能觀看錯誤信息
