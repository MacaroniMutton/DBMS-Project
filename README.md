# DBMS-Project

Hopefully we pull this off

Points to Note:

1. In settings.py, add 'myappname' in installed apps
2. In settings.py, add 'templates' in TEMPLATES DIR
3. Templates and static folders should be inside the myappname folder
4. Templates folder contains html files
5. Static folder contains images, video, audio, css, javascript
6. In every html file, add {% load static %} at the very beginning
7. Replace all urls in the html files as follows : "assets/images/riot-games.png" replaced to "{% static 'assets/images/riot-games.png' %}"

Also we have to use {% csrf_token %} somewhere, idk what it is tho