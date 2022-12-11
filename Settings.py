import configparser

class Settings:
	def __init__(self):


		self.path = "Config.ini"

		self.config = configparser.ConfigParser()

		self.DefaultSettings = {
		"Level": "Easy",
		"TryTime": str("2"),
		"NumberTries": str("15"),
		"Sounds": str("True"),
		"TypingSounds": str("True")
		}

	def WriteSettings(self, **NewSettings):

		try:
			self.config.read(self.path, encoding='utf-8')
		except:
			pass

		try:
			self.config.add_section("default")
		except configparser.DuplicateSectionError:
			pass

		for Setting in NewSettings:
			self.config.set("default", Setting, NewSettings[Setting])

		with open(self.path, "w", encoding='utf-8') as config_file:
			self.config.write(config_file)

	def ReadSettings(self):

		try:
			self.config.read(self.path, encoding='utf-8')
		except:
			self.WriteSettings(**self.DefaultSettings)

		CurrentSettings = self.DefaultSettings.copy()

		for Setting in CurrentSettings:
			try:
				CurrentSettings[Setting] = self.config.get("default", Setting)
			except:
				DefaultSetting = {Setting: self.DefaultSettings[Setting]}
				self.WriteSettings(**DefaultSetting)

		return CurrentSettings

#end of class
