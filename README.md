# AnuncioBebe — Publicar en GitHub Pages

Pasos rápidos para publicar este sitio en GitHub y obtener una URL pública (para que el QR funcione para otros):

1) Crear un repositorio en GitHub
- Ve a https://github.com y crea un nuevo repositorio (por ejemplo `AnuncioBebe`).

2) Desde tu máquina (PowerShell) en la carpeta `C:\AnuncioBebe` ejecuta:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial site for AnuncioBebe"
# reemplaza <URL-REPO> por la URL que GitHub te dará, p.e. https://github.com/tu-usuario/AnuncioBebe.git
git remote add origin <URL-REPO>
git push -u origin main
```

3) Habilitar GitHub Pages
- En el repositorio en GitHub, ve a Settings -> Pages.
- Selecciona la rama `main` (root) como fuente y guarda.
- GitHub proporcionará una URL como `https://tu-usuario.github.io/AnuncioBebe/` en unos minutos.

4) Verifica el QR
- Una vez que la página esté publicada, abre la URL pública en tu navegador.
- El QR generado en la sección "Invitación / Regalo" se actualizará automáticamente para apuntar a la URL pública cuando accedas a la página publicada.

Consejos rápidos:
- Si quieres un dominio personalizado o HTTPS obligatorio, configura un `CNAME` o usa Netlify.
- Si prefieres usar la línea de comandos para crear el repo y publicar puedes usar `gh` (GitHub CLI). Ejemplo:

```powershell
# requiere gh instalado e iniciado
gh repo create tu-usuario/AnuncioBebe --public --source=. --remote=origin --push
```

Si quieres, yo puedo:
- Generar el `README.md` (hecho).
- Crear un archivo `.gitignore` apropiado.
- Preparar un ZIP listo para enviar.
- Preparar comandos para `gh` y guiarte paso a paso.

Dime cuál prefieres y procedo.