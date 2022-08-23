@echo off
IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)
 
REM --> Si hay error es que no hay permisos de administrador.
if '%errorlevel%' NEQ '0' (
    echo Corra el programa como Administrador.
	echo De clic derecho sobre el ejecutable del programa y presione Ejecutar como Administrador.
) else (
echo Abriendo......... ^


"%~dp0\systemSGCA.py"
pause
)
    
pause
