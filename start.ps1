py main.py
cd rvc
py inference.py
Add-Type -AssemblyName presentationCore
$mediaPlayer = New-Object system.windows.media.mediaplayer
$mediaPlayer.open('./audio-outputs/output.wav')
$mediaPlayer.Play()
