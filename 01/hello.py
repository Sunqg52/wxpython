import wx

class HelloFrame(wx.Frame):
	def __init__(self, *args, **kw):
		super(HelloFrame, self).__init__(*args, **kw)

		# 新建一个窗口
		pnl = wx.Panel(self)

		# 在窗口中添加字体
		st = wx.StaticText(pnl, label="Hello World!")
		font = st.GetFont()
		font.PointSize += 10
		font = font.Bold()
		st.SetFont(font)

		# 创建一个sizer去管理布局
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(st, wx.SizerFlags().Center())
		pnl.SetSizer(sizer)

		# 创建菜单栏
		self.makeMenuBar()

		# 创建状态栏
		self.CreateStatusBar()
		self.SetStatusText("mading in chain.sunqg")

	def makeMenuBar(self):
		fileMenu = wx.Menu()

		helloItem = fileMenu.Append(-1, "&Hello...\tCrtl-H",
			"help string shown in status bar for this menu item")
		fileMenu.AppendSeparator()

		exitItem = fileMenu.Append(wx.ID_EXIT)
		helpMenu = wx.Menu()
		aboutItem = helpMenu.Append(wx.ID_ABOUT)

		menuBar = wx.MenuBar()
		menuBar.Append(fileMenu, "&File")
		menuBar.Append(helpMenu, "&Help")

		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
		self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
		self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

	def OnHello(self, event):
		wx.MessageBox("Hello again from wxPython")

	def OnExit(self, event):
		self.close(True)

	def OnAbout(self, event):
		wx.MessageBox("This is a wxPython Hello World sample",
			"About Hello World 2",
			wx.OK|wx.ICON_INFORMATION)

if __name__=='__main__':

	app = wx.App()
	frm = HelloFrame(None, title='Hello World 2')
	frm.Show()
	app.MainLoop()

