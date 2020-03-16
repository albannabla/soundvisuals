# soundvisuals

this is my first project in Django, I have used this little idea to learn how Django works and how to deploy it on Heroku via github.
the finished app can be found here:
https://dry-sea-37473.herokuapp.com/

the app generates sounds using 3 pure waves at different frequencies selected by user and then it displays graphically the resulting sound in both time and frequency domains

things that I have learned in this project:
- what is Django and how to use it, remotely and via Heroku
- how to do a Heroku deployment
- how to convert a normal html+js+php website into Django, so to integrate python scripts
- how to generate sounds using mathematical signals
- how to create charts starting from a wave file
- how to create an Aptfile to upload strange modules on Heroku (in this case the soundfile library)

things that I did not manage to fix: 
- creation of files and charts "on the fly": the app saves everything to images and wavefile, which are displayed in a different webpage...  I am still not clear if charts can be generated on the fly like I typically do with googlecharts on a js based website
- often the wavefile (which is saved into the static folder) is not re-loaded by the webpage... this is quite annyoying since there is no way to immediately tell that the sound does not relate to the waves displayed and it is also quite erratic... I have not quite figured out how to fix this issue

