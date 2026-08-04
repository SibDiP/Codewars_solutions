# Codewars Agent
On request (title, link, code solutions):

1. Create file in `codewars/`:
   - Name: `{N}_kyu_{snake_case_name}.py` (N from title/link).
   - Content: multi-line comment with title, link, description, explanations; then solution code (main + alternatives). Imports before functions.

2. Update README.md:
   - Last number in table +1 → new number.
   - Date: today (YYYY-MM-DD) if not specified.
   - File link: `https://github.com/SibDiP/Codewars_solutions/blob/main/codewars/name.py`.
   - Technologies: brief list (escape `|` as `\|`).
   - Insert row at end of table.

3. Report result. If `codewars/` missing – create. Overwrite without asking. Work directly with FS.