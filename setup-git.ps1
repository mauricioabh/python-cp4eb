# Script para configurar git y el remote
cd C:\Projects\certifications\python-cp4eb

Write-Host "1. Inicializando git..."
git init

Write-Host "2. Agregando remote origin..."
git remote remove origin 2>$null
git remote add origin https://github.com/mauricioabh/python-cp4eb.git

Write-Host "3. Verificando remote configurado:"
git remote -v

Write-Host "`n4. Estado actual:"
git status
