# Secure Coding Review Report

## Project

Flask Login System

---

## Objective

The objective of this review is to identify security vulnerabilities inside the application and recommend secure coding practices.

---

## Tools Used

- Manual Code Review
- Bandit Static Analyzer

---

# Findings

## Finding 1

### Vulnerability

SQL Injection

### Severity

Critical

### Description

The application constructs SQL queries using Python f-strings.

Example

SELECT * FROM users WHERE username='admin'

This allows attackers to inject malicious SQL.

### Recommendation

Use Parameterized Queries.

Status

Fixed

---

## Finding 2

### Vulnerability

Weak Password Hashing

### Severity

High

### Description

The application stores passwords using MD5.

MD5 is considered broken.

### Recommendation

Use werkzeug.security.generate_password_hash()

Status

Fixed

---

## Finding 3

### Vulnerability

Hardcoded Secret Key

### Severity

Medium

### Description

Secret keys should never exist inside source code.

Recommendation

Load Secret Key from Environment Variables.

Status

Fixed

---

## Finding 4

### Vulnerability

Reflected XSS

### Severity

High

Description

User input is directly rendered inside HTML.

Recommendation

Escape user input before rendering.

Status

Fixed

---

## Finding 5

### Vulnerability

Debug Mode Enabled

Severity

Medium

Description

Debug mode exposes sensitive information.

Recommendation

Disable Debug Mode in production.

Status

Fixed

---

# Conclusion

The reviewed application contained five security vulnerabilities.

All identified issues were fixed using secure coding practices.

The application now follows modern authentication and input validation standards.