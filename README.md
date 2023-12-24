# LEPortableHelper-Plus
LEPortableHelper-Plus 是我自製的一個小工具,可以將 Locale Emulator 變為攜帶式套件(也能叫 便攜式 )

他能夠讀取Locale Emulator的設定檔，在不安裝LE的情況下用語言環境執行程式

![image](https://github.com/GhostSoulGS/LEPortableHelper-Plus/assets/86374153/1b6525c0-cb0a-4609-ab92-18a03c256171)

LEPortableHelper-Plus includes English<br>
however, the explanations and tutorials do not contain English because I am not proficient in the language.<br>
I apologize for any inconvenience.

# 功能:

支持Unicode路徑

主要選項: [生成bat檔] [直接執行]

可選選項: [在目標配置LEP(Locale_Emulator文件)] [在目標配置exe] [生成相對路徑] [自訂儲存位置]

(關於具體的使用以及教學已配置在兩個PDF文件裡,有興趣的可以看一看)

# 注意:

此工具可以替換 Locale Emulator 版本 , 但是資料夾名稱固定為 Locale_Emulator (替換的資料至少需要安裝並移除一次)

[相對路徑]生成的bat不可以移動位置,一旦移動位置就會失效,要再使用必須修改路徑才行

# 契機:
LEPortableHelper-Plus 是我受到了 [LEPortableHelper](https://github.com/wuliou/LEPortableHelper) 啟發後自製的小工具

原理有一部份是一樣的,只是我改善功能後將介面徹底翻新並換上了較新的Python3.11.5版本而已(也因此跟win7不相容了)
