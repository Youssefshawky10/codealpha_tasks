# CodeAlpha Secure Coding Review

## Project Description

This project demonstrates a secure coding review of a vulnerable Flask web application.

The objective was to identify common web security vulnerabilities, fix them, and document the remediation process.

---

## Vulnerabilities

- SQL Injection
- Weak Password Hashing
- Hardcoded Secret Key
- Reflected XSS
- Debug Mode Enabled

---

## Technologies

- Python
- Flask
- SQLite
- Bandit

---

## Static Analysis

```bash
bandit vulnerable_app.py
```

---

## Run

```bash
python init_db.py

python vulnerable_app.py
```

Secure Version

```bash
python fixed_app.py
```

---

## Folder Structure

```
CodeAlpha_Secure_Coding_Review/

vulnerable_app.py

fixed_app.py

security_review_report.md

README.md

requirements.txt
```

---

## Author

Youssef Shawky