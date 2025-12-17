@echo off
REM - Script para empujar cambios a GitHub desde C:\AnuncioBebe
@echo off
REM Script para empujar cambios a GitHub desde C:\AnuncioBebe
cd /d "%~dp0"

echo Carpeta de trabajo: %CD%

REM Verificar git instalado
git --version >nul 2>&1
if errorlevel 1 (
	echo Git no detectado en esta carpeta. Asegurate de tener Git instalado y que esta carpeta sea un repositorio.
	pause
	exit /b 1
)

echo Verificando estado de git...
git status --porcelain

echo Añadiendo cambios...
git add .

echo Commit (mensaje por defecto: "Update site")
git commit -m "Update site" 2>nul || echo No hay cambios para commitear.

echo Comprobando remote origin...
git remote get-url origin 2>nul
if errorlevel 1 (
	echo No existe remote 'origin'.
	echo Si ya creaste el repo en GitHub pega aqui la URL (ej: https://github.com/tu-usuario/anuncio-bb.git) y pulsa Enter:
	set /p repoUrl=Remote URL: 
	if "%repoUrl%"=="" (
		echo No se proporciono URL. Saliendo.
		pause
		exit /b 1
	)
	git remote add origin %repoUrl%
)

echo Empujando a origin main...
git branch -M main
git push -u origin main
if errorlevel 1 (
	echo Error al empujar. Puedes intentar usar GitHub Desktop o comprobar tus credenciales.
) else (
	echo Push completado con exito.
)

echo Hecho.
pause
nif %errorlevel% neq 0 (