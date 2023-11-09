@echo off

REM Download the file from GitHub
echo Downloading file from GitHub...
curl -o %APPDATA%\GIMP\2.10\plug-ins\picwish_colorize.py https://raw.githubusercontent.com/ZYR0Z/ai-colorization-gimp/master/picwish-colorize.py

REM Check if the download was successful

echo Download successful.
REM Prompt the user for an API key
set /p api_key=Paste your API key here and press Enter: 
set "api_key_file=%APPDATA%\GIMP\2.10\plug-ins\colorize_api_key.json"
mkdir "%APPDATA%\GIMP\2.10\plug-ins"
echo {"api_key": "%api_key%"} > "%api_key_file%"
echo Success! Restart GIMP to use the Plugin!

REM Prompt the user to press any key to close
pause

