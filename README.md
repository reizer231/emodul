# emodul

Hello,
files description:

Temp_set_API_POST.py -> Script created for collecting data from emodul API (Heater controller) extracting it and passing to HomeAssistant API.
Script being ran every 5 minutes (via crontabs) on server which is running on same terminal as HA (PROXMOX VE)

fireup_toggle.py -> Script which will help you to toggle (click) on specific tile. I used Xpath to navigate selenium firefox driver to execute demanded action - gecko driver needed in path specified.

list for some checked xpaths - I've listed some xpaths which I tested in order to trigger something.

If any questions you can reach me over marcin@go-te.ch.
