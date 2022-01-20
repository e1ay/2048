from settingscreen import SettingScreen, click_img
import settings
settings.player_name = input('Input your name:  (player-standard)')
r = SettingScreen(50, 450, click_img, 0.1)
r.show_screen()