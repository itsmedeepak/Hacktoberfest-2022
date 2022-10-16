# Trello-Mail.app-Automator-Script
================================

An Apple Automator script that allows a hotkey to be used to create a card in Trello 

### Create your automator script:
* Run Automator
* Choose Service
* Service receives "no input" in "Mail"
* Drag "Run Applescript" to the workflow
* Replace 	(* Your script goes here *) with the contents of the Applescript file
* Get an application key at https://trello.com/1/appKey/generate
* Get a token at https://trello.com/1/authorize?key=**YOURKEY**&name=**YOURAPP**&expiration=never&response_type=token&scope=read,write) - note it is a never expiring token so be careful
* Edit the Applescript accordingly with your application key and token.
* Save the service (⌘S) and give it a name.

### Create your keyboard shortcut:
* Run System Preferences -> Keyboard -> Keyboard Shortcuts
* Choose Application Shortcuts, hit the + button:
* * Application: Mail
* * Menu Title: The name of your Automator Service as seen in the Mail->Services menu
* * Keyboard Shortcut: Your choice, I use ⌘T 
* * Click Add

All set!
