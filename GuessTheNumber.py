# import project libraries.
import wx
import random
import accessible_output2.outputs.auto
import configparser
import pywinmm
import webbrowser
from Settings import Settings

global GameSettings
GameSettings = Settings().ReadSettings()


# Create app with wx.
app= wx.App()

class GuessTheNumber(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title = 'guess the number', size=(230, 180))

		#make window in center.
		self.Center()

		#make window Minimum size.
		self.Maximize(False)
		self.EnableMaximizeButton(False)

		#set window Direction
		self.SetLayoutDirection(wx.Layout_LeftToRight)

		# Creating panel
		self.Panel = wx.Panel(self)

		# Creating Buttons
		self.StartGame = wx.Button(self.Panel, -1, "Start the game", pos=(20,20), size=(100,30))
		self.ChangeOptions = wx.Button(self.Panel, -1, "Change options", pos=(20,70), size=(100,30))
		self.more = wx.Button(self.Panel, -1, "more", pos=(130,20), size=(60,30))
		self.Close = wx.Button(self.Panel, -1, "Close", pos=(130,70), size=(60,30))

		# Show Main window
		self.Show()

		# events.
		self.StartGame.Bind(wx.EVT_BUTTON, self.OnStart)
		self.Close.Bind(wx.EVT_BUTTON, self.OnCloseProgram)
		self.ChangeOptions.Bind(wx.EVT_BUTTON, self.OnChange)
		self.more.Bind(wx.EVT_BUTTON, self.OnMore)


	def OnMore(self, event):
		MoreMenu = wx.Menu()
		ContactMenu = wx.Menu()
		QaisMenu = wx.Menu()
		QaisEm = QaisMenu.Append(-1, "&E-mail")
		QaisTe =QaisMenu.Append(-1, "&Telegram")
		QaisWh =QaisMenu.Append(-1, "&Whats App")
		QaisTw =QaisMenu.Append(-1, "&Twitter")
		QaisFa =QaisMenu.Append(-1, "&Facebook")
		ContactMenu.AppendSubMenu(QaisMenu, "&Qais Alrefai")
		MahmoodMenu = wx.Menu()
		MahmoodEm =MahmoodMenu.Append(-1, "&E-mail")
		MahmoodTe =MahmoodMenu.Append(-1, "&Telegram")
		MahmoodWh =MahmoodMenu.Append(-1, "&Whats App")
		MahmoodTw =MahmoodMenu.Append(-1, "&Twitter")
		MahmoodFa =MahmoodMenu.Append(-1, "&Facebook")
		ContactMenu.AppendSubMenu(MahmoodMenu, "&Mahmood atef")
		MesterPerfectMenu = wx.Menu()
		MesterPerfectEm =MesterPerfectMenu.Append(-1, "&E-mail")
		MesterPerfectTe =MesterPerfectMenu.Append(-1, "&Telegram")
		MesterPerfectWh =MesterPerfectMenu.Append(-1, "&Whats App")
		MesterPerfectTw =MesterPerfectMenu.Append(-1, "&Twitter")
		MesterPerfectFa =MesterPerfectMenu.Append(-1, "&Facebook")
		ContactMenu.AppendSubMenu(MesterPerfectMenu, "&Ahmed Bakr")
		TecWindow=ContactMenu.Append(-1, "TecWindow on Telegram")
		MoreMenu.AppendSubMenu(ContactMenu, "&Contact us")
		self.AboutItem = MoreMenu.Append(-1, "About")
		self.CloseProgramItem = MoreMenu.Append(-1, "Close program")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("mailto:ww258148@gmail.com"), QaisEm)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/QaisAlrefai"), QaisTe)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/qais_Alrefai"), QaisTw)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/962792540394"), QaisWh)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/Qais1461"), QaisFa)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("mailto:mahmoud.atef.987123@gmail.com"), MahmoodEm)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/MahmoodAtef"), MahmoodTe)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/mahmoud_atef999"), MahmoodTw)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/201224660664"), MahmoodWh)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/mahmoud.atef.000"), MahmoodFa)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("mailto:AhmedBakr593@gmail.com"), MesterPerfectEm)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/MesterPerfect"), MesterPerfectTe)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/my_nvda"), MesterPerfectTw)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/201554240991"), MesterPerfectWh)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/my.nvda.1"), MesterPerfectFa)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/TecWindowProjects"), TecWindow)
		self.Bind(wx.EVT_MENU, self.OnAboutProgram, self.AboutItem)
		self.Bind(wx.EVT_MENU, self.OnCloseProgram, self.CloseProgramItem)
		self.PopupMenu(MoreMenu)



#creating OnAboutProgram function to show information about this program.
	def OnAboutProgram(self, event):
		AboutDialog = wx.MessageDialog(self, """Guess the number.
Version: 1.1.
This game was developed by:
Ahmed Bakr.
Qais Alrifai.
Mahmoud Atef.""", "About the program", style=wx.ICON_INFORMATION+wx.OK)
		AboutDialog.SetOKLabel("&Ok")
		AboutDialog.ShowModal()



	def OnChange(self, ev):
		GameOptions(self)

	def OnStart(self, ev):
		Play(self)
		self.Hide()

	def OnCloseProgram(self, event):
		wx.Exit()




class GameOptions(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, title="Game Options", size=(400, 250))
		#make window in center.
		self.Center()
		#make window Minimum size.
		self.Maximize(False)
		#set window Direction
		self.SetLayoutDirection(wx.Layout_LeftToRight)

		# Creating panel
		Panel = wx.Panel(self)



		wx.StaticText(Panel, -1, "Choose the level:", pos=(20,20), size=(380, 30))
		self.Level = wx.ComboBox(Panel, -1, choices=['Easy', 'Normal', 'Hard',], pos=(20, 50), size=(120, 40), style=wx.CB_READONLY)
		self.Level.Value = GameSettings["Level"]

		wx.StaticText(Panel, -1, "Select the number of tries:", pos=(150,20), size=(380, 30))
		self.NumberTries = wx.SpinCtrl(Panel, -1, "15", min=1, max=200, style=wx.SP_ARROW_KEYS, pos=(160, 50), size=(50, 20))
		self.NumberTries.Value = GameSettings["NumberTries"]


		wx.StaticText(Panel, -1, "Select the allowed time  in minutes::", pos=(140,80), size=(200, 30))
		self.TryTime = wx.SpinCtrl(Panel, -1, "2", min=1, max=10, style=wx.SP_ARROW_KEYS, pos=(170, 110), size=(50, 20))
		self.TryTime.Value = GameSettings["TryTime"]

		self.sounds = wx.CheckBox(Panel, -1, label="Enable trying sounds:", pos=(10, 80), size=(140, 30))
		self.sounds.Value = eval(GameSettings["Sounds"])

		self.TypingSounds = wx.CheckBox(Panel, -1, label="Enable typing sounds", pos=(10, 110), size=(140, 30))
		self.TypingSounds.Value = eval(GameSettings["TypingSounds"])


		self.Close = wx.Button(Panel, wx.ID_CANCEL, "Close", pos=(50,150), size=(60,30))
		self.Close.SetDefault()


		self.Show()



		self.Close.Bind(wx.EVT_BUTTON, self.OnCloseWindow)


	def OnCloseWindow(self, event):
		global GameSettings
		GameSettings = {
		"Level": self.Level.Value,
		"TryTime": str(self.TryTime.Value),
		"NumberTries": str(self.NumberTries.Value),
		"Sounds": str(self.sounds.Value),
		"TypingSounds": str(self.TypingSounds.Value),
}
		Settings().WriteSettings(**GameSettings)

		self.Destroy()



class Play(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title = 'Play guess the number', size=(500, 500))

		#make window in center.
		self.Center()

		#make window Minimum size.
		self.Maximize(False)
		self.EnableMaximizeButton(False)

		#set window Direction
		self.SetLayoutDirection(wx.Layout_LeftToRight)

		self.o = accessible_output2.outputs.auto.Auto()
		self.RandomNumber = self.RandomNumbers()
		self.Tries = 0
		self.Failed = ""
		self.RemainingTrise = int(GameSettings["NumberTries"])
		self.IDRemainingTrise = wx.NewIdRef(count=1)
		self.IDElapsedTime = wx.NewIdRef(count=1)
		self.IDRemainingTime = wx.NewIdRef(count=1)
		self.IDInstructions = wx.NewIdRef(count=1)
		self.IDResult = wx.NewIdRef(count=1)
		self.IDTries = wx.NewIdRef(count=1)
		self.time = int(GameSettings["TryTime"])*60
		self.MainWindow = parent
		self.Result = "Start Guessing."

		# Creating panel
		self.Panel = wx.Panel(self)

		self.status = wx.StatusBar(self, -1)
		self.status.SetFieldsCount(3)
		self.status.SetStatusText("no result", 0)
		self.status.SetStatusText(self.ConvertSeconds(self.time), 1)
		self.status.SetStatusText(str(self.RemainingTrise), 2)
		self.status.SetStatusWidths([-3, -2, -1])
		self.SetStatusBar(self.status)

		self.Info = wx.StaticText(self.Panel, -1, "", pos=(190,70), size=(380, 30))
		self.CurrentNumber = wx.SpinCtrl(self.Panel, -1, "", style=wx.SP_WRAP+wx.ALIGN_LEFT, pos=(30, 290), size=(50, 20))
		if GameSettings["Level"] == "Easy":
			#self.CurrentNumber.SetMin(0)
			self.CurrentNumber.SetMax(999)
			self.Min = 100
			self.Max = 999
			self.NumberOfDigits = 3
		elif GameSettings["Level"] == "Normal":
			#self.CurrentNumber.SetMin(0)
			self.CurrentNumber.SetMax(9999)
			self.Min = 1000
			self.Max = 9999
			self.NumberOfDigits = 4
		elif GameSettings["Level"] == "Hard":
			#self.CurrentNumber.SetMin(0)
			self.CurrentNumber.SetMax(99999)
			self.Min = 10000
			self.Max = 99999
			self.NumberOfDigits = 5
		self.CurrentNumber.SetValue("")



		self.Close = wx.Button(self.Panel, -1, "Close", pos=(450,250), size=(60,30))



		self.CantTrye = "You can't try anymore"
		self.TimeEnd = "You don't have time anymore"
		self.Instructions = F"In {self.ConvertSeconds(self.time)} and {self.RemainingTrise} Tries, try to find the correct number between {self.Min} and {self.Max}."
		self.Info.SetLabel(self.Instructions)



		# events.
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
		self.timer.Start(1000)
		self.CurrentNumber.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
		self.Bind(wx.EVT_TEXT, self.OnPlay, self.CurrentNumber)
		self.Close.Bind(wx.EVT_BUTTON, self.OnCloseProgram)
		self.Bind(wx.EVT_MENU, lambda ev: self.o.speak(self.ConvertSeconds(self.time), interrupt=True), self.IDRemainingTime)
		self.Bind(wx.EVT_MENU, lambda ev: self.o.speak(self.ConvertSeconds(int(GameSettings["TryTime"])*60 - self.time), interrupt=True), self.IDElapsedTime)
		self.Bind(wx.EVT_MENU, lambda ev: self.o.speak(F"{self.Instructions}.", interrupt=True), self.IDInstructions)
		self.Bind(wx.EVT_MENU, lambda ev: self.o.speak(F"{self.Result}", interrupt=True), self.IDResult)
		self.Bind(wx.EVT_MENU, lambda ev: self.o.speak(F"You tryed {self.Tries} times.", interrupt=True), self.IDTries)
		self.Bind(wx.EVT_MENU, lambda ev: self.o.speak(F"Remaining Trise: {self.RemainingTrise}.", interrupt=True), self.IDRemainingTrise)
		self.Bind(wx.EVT_CLOSE, self.OnClose)

		self.Show()

		self.hotKeys = wx.AcceleratorTable([
		(0, ord("R"), self.IDRemainingTrise),
		(0, ord("I"), self.IDInstructions),
		(0, ord("Y"), self.IDResult),
		(0, ord("U"), self.IDTries),
		(0, ord("T"), self.IDRemainingTime),
		(0, ord("E"), self.IDElapsedTime)
		])
		self.SetAcceleratorTable(self.hotKeys)

	def onKeyDown(self, event):
		event.Skip()
		if event.GetKeyCode() == wx.WXK_BACK:
			self.OnDelete(None)



	def OnDelete(self, event):
		if GameSettings["TypingSounds"]:
			pywinmm.load("sounds/Delete.wav").play()
		self.CurrentNumber.SetValue("")


	def RandomNumbers(self):
		if GameSettings["Level"] == "Easy":
			self.Random = random.randint(100,999)
		elif GameSettings["Level"] == "Normal":
			self.Random = random.randint(1000,9999)
		elif GameSettings["Level"] == "Hard":
			self.Random = random.randint(10000,99999)
		return self.Random



	def OnPlay(self, ev):
		Elapsed = self.ConvertSeconds(int(GameSettings["TryTime"])*60 - self.time)

		if len(str(self.CurrentNumber.Value)) == self.NumberOfDigits:
			pass
		elif GameSettings["TypingSounds"]:
			pywinmm.load("sounds/Typing.wav").play()
		if len(str(self.CurrentNumber.Value)) == self.NumberOfDigits:
			self.Tries += 1
			if int(GameSettings["NumberTries"]) == self.Tries:
				self.Failed = F"Unfortunately, you failed to find the correct number, the correct number is {self.RandomNumber}."
				self.Result = self.Failed
				if GameSettings["Sounds"] == "True":
					pywinmm.load("sounds/fail.wav").play()
				self.o.speak(F"{self.CantTrye}, {self.Result}", interrupt=True)
				self.CurrentNumber.Value = ""
				self.RandomNumber = self.RandomNumbers()
				self.RemainingTrise = int(GameSettings["NumberTries"])
				self.Tries = 0
				self.time = int(GameSettings["TryTime"])*60
				self.Instructions = F"In {self.ConvertSeconds(self.time)} and {self.RemainingTrise} Tries, try to find the correct number between {self.Min} and {self.Max}."
				self.o.speak(F"{self.Instructions}", interrupt=False)
			elif self.CurrentNumber.Value == self.RandomNumber:
				self.Success =F"Well done, the correct number is {self.RandomNumber}, you found it in {Elapsed} and {self.Tries} tries."
				self.Result = self.Success
				if GameSettings["Sounds"] == "True":
					pywinmm.load("sounds/correct.wav").play()
				self.o.speak(F"{self.Result}", interrupt=True)
				self.CurrentNumber.Value = ""
				self.time = int(GameSettings["TryTime"])*60
				self.RandomNumber = self.RandomNumbers()
				self.RemainingTrise = int(GameSettings["NumberTries"]) 
				self.Tries = 0
				self.Instructions = F"In {self.ConvertSeconds(self.time)} and {self.RemainingTrise} Tries, try to find the correct number between {self.Min} and {self.Max}."
				self.o.speak(F"{self.Instructions}", interrupt=False)
			elif self.CurrentNumber.Value < self.RandomNumber:
				self.Greater = F"The correct number is greater than {self.CurrentNumber.Value}."
				self.Result = self.Greater
				if GameSettings["Sounds"] == "True":
					pywinmm.load("sounds/error.wav").play()
				self.o.speak(F"{self.Result}", interrupt=True)
				self.RemainingTrise -= 1
				self.CurrentNumber.Value = ""
			elif self.CurrentNumber.Value > self.RandomNumber:
				self.Less = F"The correct number is less than {self.CurrentNumber.Value}."
				self.Result = self.Less
				if GameSettings["Sounds"] == "True":
					pywinmm.load("sounds/error.wav").play()
				self.o.speak(F"{self.Result}", interrupt=True)
				self.RemainingTrise -= 1
				self.CurrentNumber.Value = ""

		self.status.SetStatusText(self.Result, 0)
		self.status.SetStatusText(str(self.RemainingTrise), 2)

	def OnTimer(self, event):
		if not self.time:
			self.Failed = F"Unfortunately, you failed to find the correct number, the correct number is {self.RandomNumber}."
			self.Result = F"{self.TimeEnd}, {self.Failed}"
			self.o.speak(F"{self.Result}", interrupt=False)
			self.RandomNumber = self.RandomNumbers()
			self.RemainingTrise = int(GameSettings["NumberTries"])
			self.Tries = 0
			self.time = int(GameSettings["TryTime"])*60
			self.Instructions = F"In {self.ConvertSeconds(self.time)} and {self.RemainingTrise} Tries, try to find the correct number between {self.Min} and {self.Max}."
			self.Info.SetLabel(self.Instructions)
			self.o.speak(F"{self.Instructions}", interrupt=False)
			if GameSettings["Sounds"] == "True":
				pywinmm.load("sounds/fail.wav").play()
			self.CurrentNumber.Value = ""
		else:
			self.time -= 1
			self.Instructions = F"In {self.ConvertSeconds(self.time)} and {self.RemainingTrise} Tries, try to find the correct number between {self.Min} and {self.Max}."
			self.Info.SetLabel(self.Instructions)

		self.status.SetStatusText(self.ConvertSeconds(self.time), 1)

	def ConvertSeconds(self, time:int):
		seconds = time%60
		minute = int(time/60)
		result = "{}minutes and {} seconds".format(minute,seconds)
		if minute < 1:
			result = "{} seconds".format(seconds)
		return result


	def OnCloseProgram(self, event):
		wx.Exit()

	def OnClose(self, event):
		self.Destroy()
		self.MainWindow.Show()

GuessTheNumber()
app.MainLoop()    