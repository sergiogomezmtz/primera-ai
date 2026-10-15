#!/usr/bin/env python3
"""Verificación local, offline y multiplataforma del mentor y su camino dorado.

Uso desde la raíz: python3 verificar.py (macOS/Linux) o py verificar.py (Windows).
No valida un modelo real, credenciales, sandbox ni readiness live.
"""
from __future__ import annotations
import os
import re
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 90

def run(label, command, expected_exit=0, must_contain=None):
    env = os.environ.copy(); env['PYTHONDONTWRITEBYTECODE'] = '1'
    try:
        result = subprocess.run(command, cwd=ROOT, env=env, text=True, capture_output=True, timeout=TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        print(f'[FAIL] {label} (timeout>{TIMEOUT_SECONDS}s)'); return False
    except OSError as exc:
        print(f'[FAIL] {label} (no se pudo ejecutar: {exc})'); return False
    combined = result.stdout + result.stderr
    ok = result.returncode == expected_exit and (must_contain is None or must_contain in combined)
    status = 'PASS' if ok else 'FAIL'
    print(f'[{status}] {label} (exit={result.returncode}, esperado={expected_exit})')
    if not ok: print(combined[-3000:])
    return ok

def check_links():
    missing = []
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts: continue
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            target = target.split('#', 1)[0].strip()
            if not target or target.startswith(('#','/','mailto:')) or '://' in target: continue
            if not (path.parent / target).resolve().exists(): missing.append(f'{path.relative_to(ROOT)} -> {target}')
    if missing:
        print('[FAIL] enlaces locales rotos'); print('\n'.join(missing)); return False
    print('[PASS] enlaces locales'); return True

def main():
    python = sys.executable
    checks = [
        ('pruebas reproducibles', [python,'-m','unittest','ejemplo.test_camino_dorado','-q'], 0, 'OK'),
        ('pruebas estructurales de /rumbo', [python,'-m','unittest','test_rumbo_comparar','-q'], 0, 'OK'),
        ('fixtures de /rumbo', [python,'-I','.claude/skills/rumbo/fixtures/comparar.py'], 0, 'CRITERIO DE SALIDA: PASA'),
        ('camino dorado v0 núcleo', [python,'ejemplo/camino_dorado.py','--modo','offline','--version','v0','--suite','nucleo'], 1, 'TASA: 4/6'),
        ('camino dorado v1 núcleo', [python,'ejemplo/camino_dorado.py','--modo','offline','--version','v1','--suite','nucleo'], 0, 'TASA: 6/6'),
        ('camino dorado v0 extendida', [python,'ejemplo/camino_dorado.py','--modo','offline','--version','v0','--suite','extendida'], 1, 'TASA: 7/10'),
        ('camino dorado v1 extendida', [python,'ejemplo/camino_dorado.py','--modo','offline','--version','v1','--suite','extendida'], 0, 'TASA: 10/10'),
    ]
    results = [run(*check) for check in checks]; results.append(check_links())
    try: git = subprocess.run(['git','diff','--check'], cwd=ROOT, text=True, capture_output=True, timeout=TIMEOUT_SECONDS); git_ok = git.returncode == 0
    except (OSError, subprocess.TimeoutExpired): git = None; git_ok = False
    git_status = 'PASS' if git_ok else 'FAIL'
    print(f'[{git_status}] git diff --check')
    if not git_ok and git is not None: print(git.stdout + git.stderr)
    results.append(git_ok)
    print('\nAlcance: verificación offline del repo; no valida modelo real, live, sandbox ni producción.')
    print(f'Resultado: {sum(results)}/{len(results)} checks pasan')
    return 0 if all(results) else 1

if __name__ == '__main__': raise SystemExit(main())
