@echo OFF

call submit_aff.bat %*
echo _______________________________________________________________________
echo Debut de l'execution du script...
date /T
time /T
echo _______________________________________________________________________

rem Mode TEST
if "%TOM_JOB_EXEC%" == "TEST" (
	echo Job execute en mode TEST
	%ABM_BIN%\tsend -sT -r0 -m"Traitement termine (mode TEST)"
	%ABM_BIN%\vtgestlog
	goto FIN
)


set PROJECT_PATH=%TOM_HOME%\SCRIPTS\AzureDataFactory\

REM Vérifie si 3 arguments sont passés
IF "%~3"=="" (
    REM Execute without params
	echo "%PROJECT_PATH%\.venv\Scripts\python %PROJECT_PATH%\azureDataFactory.py --factory %1 --pipeline %2"
	%PROJECT_PATH%\.venv\Scripts\python %PROJECT_PATH%\azureDataFactory.py --factory %1 --pipeline %2
	set RETCODE=%ERRORLEVEL%
) ELSE (
	REM Execute with params
	echo "%PROJECT_PATH%\.venv\Scripts\python %PROJECT_PATH%\azureDataFactory.py --factory %1 --pipeline %2 --params %3"
	%PROJECT_PATH%\.venv\Scripts\python %PROJECT_PATH%\azureDataFactory.py --factory %1 --pipeline %2 --params %3
	set RETCODE=%ERRORLEVEL%
)

if %RETCODE% equ 0 goto TERMINE
goto ERREUR

:ERREUR
%ABM_BIN%\tsend -sE -r%RETCODE% -m"Traitement en erreur (%RETCODE%)"
%ABM_BIN%\vtgestlog
echo _______________________________________________________________________
echo Fin d'execution du script
date /T
time /T
echo Exit [%RETCODE%]
echo _______________________________________________________________________
if not "%TOM_LOG_ACTION%"=="   " call Gestlog_wnt.bat
exit %RETCODE%

:TERMINE
%ABM_BIN%\tsend -sT -r%RETCODE% -m"Traitement termine (%RETCODE%)"
%ABM_BIN%\vtgestlog
echo _______________________________________________________________________
echo Fin d'execution du script
date /T
time /T
echo Exit [%RETCODE%]
if not "%TOM_LOG_ACTION%"=="   " call Gestlog_wnt.bat
exit %RETCODE%

:FIN
