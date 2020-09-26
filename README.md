# HoloLive-Recorder
<br>
<b>Program for recording HoloLive live streams so that you don't miss non archived streams</b>
<br>
Has Coco as default
<br><br>
<b>In order to add another channel:</b>
<br>
Copy Coco.py and rename the file to the name of the VTuber you want to record
<br>
Change the url in the script to the url of the new VTuber
<br>
Change the file_name variable to reflect the new VTuber
<br>
Add a new os.system() call to the new VTuber.py file in Main.py in the job() function
<br><hr>
<b>Requirements:</b>
<br>
<a href="https://github.com/pycontribs/tendo">tendo</a>
<br>
<a href="https://github.com/dbader/schedule">schedule</a>
<br>
<a href="https://github.com/streamlink/streamlink">streamlink</a>
