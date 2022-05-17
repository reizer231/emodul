# emodul

Hello,
files description:

Temp_set_API_POST.py -> Script created for collecting data from emodul API (Heater controller) extracting it and passing to HomeAssistant API.
Script being ran every 5 minutes (via crontabs) on server which is running on same terminal as HA (PROXMOX VE)

![PANEL](https://github.com/reizer231/emodul/blob/main/Screenshot%202022-05-17%20at%2011.36.14.png)

fireup_toggle.py -> Script which will help you to toggle (click) on specific tile. I used Xpath to navigate selenium firefox driver to execute demanded action - gecko driver needed in path specified.


![SCRIPT](https://github.com/reizer231/emodul/blob/main/Screenshot%202022-05-17%20at%2011.37.33.png)


list for some checked xpaths - I've listed some xpaths which I tested in order to trigger something.

If any questions you can reach me over marcin@go-te.ch.
