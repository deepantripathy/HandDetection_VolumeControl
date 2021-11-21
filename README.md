# HandDetection_VolumeControl

The project was created to control volume of PC or laptop via hand detection. When you close all fingers of your hands the volume is set to 0. The volume increases gradually as you let go of the fingers of your hands. The movement of hand is detected via the webcam attached. The distance is calculated between thumb tip and index finger. The distance is mapped between thumb tip and index finger with volume range. In my case range of 15 – 220 and the volume range of -63.5 - 0 was taken.

Python Libraries required:
a. CV2\
b. Mediapipe\
c. cast and POINTER form ctypes\
d. AudioUtilities and IAudioEndpointVolume\
e. numpy\
