import wx

"""
wxpython程序没有main函数，而是由wx.App衍生出的wx.AppConsole.OnInit来实现入口函数的功能
OnInit函数与早期的wxpython版本不同：不再返回框架，而是返回一个bool值来决定程序是否继续执行
尽可能的将其放置于父级框架
紧急情况下wx.Exit也可以关闭程序

"""
class DerivedApp(wx.App):
	def OnInit(self):
		the_farme = wx.Frame(None, -1)
		the frame.Show(True)
		return True


"""
其他退出程序：
wx.Window.Close(self, force=False) return bool：只有单个顶级窗口时使用，进行退出，安全的销毁窗口 不会立即破坏
wx.PyApp.SetExitOnFrameDelete(self,flag) return bool: 由编程人员指定，是否在关闭顶级窗口时退出
wx.AppConsole.OnExit() return int: 应用于wxWidgets清理之前，所有应用程序销毁之后。如果init失败，不会调用它，返回一个整型
"""