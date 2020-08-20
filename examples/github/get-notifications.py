from github import Github
from github_token import GITHUB_TOKEN, user, password

from inky import InkyPHAT

inky_display = InkyPHAT("red")

# Set up the display
if colour == "auto":
    from inky.auto import auto
    inky_display = auto()
    colour = inky_display.colour
else:
    inky_display = InkyPHAT(colour)

inky_display.set_border(inky_display.BLACK)

inky_display.v_flip = True

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

user = g2.get_user()
notifications = user.get_notifications()
print(notifications)
for notification in notifications:
	print (notification)
