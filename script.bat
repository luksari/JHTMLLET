@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
:menu
cls
echo "=======MENU======="
echo "| [1] - Dane     |"
echo "| [2] - Backup   |"
echo "| [3] - Raport   |"
echo "| [4] - Powtorz  |"
echo "| [q] - Wyjscie  |"
echo "=================="
:zapytanie

set /p odp=Wybierz opcje? 
if %odp%==1 goto dane
if %odp%==2 goto backup
if %odp%==3 goto raport
if %odp%==4 goto menu
if %odp%==q goto wyjscie
if not %odp%==1 goto menu
if not %odp%==2 goto menu
if not %odp%==3 goto menu
if not %odp%==4 goto menu
if not %odp%==q goto menu
if not exist ./in (
  if not exist ./out(
    goto dirnotexist
  )
)
if not exist JHTMLLET.exe (
  goto exenotexist
)
if not exist server.py (
  goto pynotexist
)


goto zapytanie

:dane
echo ==========Generowanie raportu danych==========
FOR %%F IN (./in/*.html) DO (
set "outname=%%F"
"JHTMLLET.exe" ./in/%%F ./out/out!outname:~2!
)
pause
goto menu

:backup
echo ==========Tworzenie kopii zapasowej raportu==========
if not exist "./backup/raport[%DATE%][%TIME:~0,2%][%TIME:~3,2%].html" (
  cd ./raport
  xcopy "raport.html" "../backup/raport[%DATE%][%TIME:~0,2%][%TIME:~3,2%].html" /f /j /w /z /d
  echo  "Zapisano w lokalizacji ./backup/raport[%DATE%][%TIME:~0,2%][%TIME:~3,2%].html"
)


pause
goto menu

:raport
echo ==========Tworzenie raportu z danych==========
py server.py
pause
goto menu

:dirnotexist
echo ==========Foldery IN i OUT nie istnieją==========
pause
goto menu

:exenotexist
echo ==========Plik wykonywalny JHTMLLET.exe nie istnieje==========
pause
goto menu

:pynotexist
echo ==========Skrypt server.py nie istnieje==========
pause
goto menu

:wyjscie
echo ==========Do zobaczenia==========
pause
