# Handoff

## Project
Teaching materials for the course **Programska oprema pri pouku** (Programming Software in Class), written primarily in Slovenian. Current lesson topic: functions.

## Recent work
- Expanded `README.md` with a table of contents, a lesson overview, and a primary-school programming refresher.
- Created `PregledSnovi.tex`, a standalone LaTeX document containing the README material, linked section entries, and tables.
- Editor diagnostics reported no errors for `PregledSnovi.tex`.

## Git status at handoff
- Branch: `main`; it was up to date with `origin/main` at the last status check.
- `README.md` is modified and unstaged.
- `PregledSnovi.tex` is untracked.
- LaTeX build outputs are also untracked: `.aux`, `.fdb_latexmk`, `.fls`, `.log`, `.out`, `.pdf`, and `.synctex.gz`.
- No changes have been committed or pushed since these current edits. Review and stage only the intended files; consider whether generated LaTeX artifacts should be ignored before committing.

## Suggested next steps
1. Inspect the README and LaTeX output, especially the README overview table header.
2. Decide whether to keep the generated PDF in version control; normally exclude temporary LaTeX build files.
3. If requested, add a suitable `.gitignore`, then commit and push the intended documentation changes.
