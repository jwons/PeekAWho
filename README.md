# PeekAWho

Devpost page for this project can be found [here](https://devpost.com/software/peekawho)

## Inspiration

Sometimes people stop by your dorm room, apartment, or house looking for you but you aren't there but you don't know that they were there. There should be a way of fixing that.


## What it does

Our project is in its very early stages. It currently is a program that notifies a user when their friends stop by. It tells the user who exactly stopped by using facial recognition and when they stopped by. It currently uses a webcam now but in the future it will use a camera attached to a raspberry pi. For demo purposes, the notifications currently utilize the standard Microsoft Windows notifications.

## Operation

To use, the server is run on the user's computer. The client is then run on the device attached to the camera. The client upon initial startup will read a folder of faces to "learn" them. When one of those faces appears at the camera, a notification is sent to the user stating that person's name, and that they are at the front door. Unknown faces will prompt no response. A known face has to be absent from the camera's view for at least 5 minutes to prompt another notification to be sent to the user, to prevent notification spamming. 
