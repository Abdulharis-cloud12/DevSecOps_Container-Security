# 🛡️ DevSecOps Container Security Pipeline

A beginner-friendly introductory **DevSecOps** project that demonstrates how security can be integrated into a Continuous Integration (CI) pipeline using **GitHub Actions**, **Gitleaks**, and **Trivy**.

Instead of performing security checks manually, this project automates them every time code is pushed to the repository, introducing the core concepts of **Shift Left Security** and **Security Gates**.

---

## 📌 Project Goal

The goal of this project is to build a secure CI pipeline that automatically:

- Detects accidentally committed secrets
- Scans Docker images for vulnerabilities
- Stops insecure builds before deployment
- Demonstrates the fundamentals of DevSecOps automation

This project serves as an introductory hands-on implementation of modern DevSecOps practices.

---

## 🎯 Learning Objectives

By completing this project, I aim to learn:

- GitHub Actions fundamentals
- CI/CD workflow automation
- Secret scanning using Gitleaks
- Container vulnerability scanning using Trivy
- Security Gates
- Docker image hardening
- Reading and interpreting vulnerability reports
- DevSecOps pipeline design

---

## 🛠️ Tech Stack

| Category | Tool |
|----------|------|
| Language | Python |
| Framework | Flask |
| Containerization | Docker |
| Version Control | Git & GitHub |
| CI/CD | GitHub Actions |
| Secret Scanning | Gitleaks |
| Container Security | Trivy |

---

# 📂 Project Structure

```text
devsecops-container-security-pipeline/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# 🏗️ Project Architecture

```
                Developer

                    │

                Git Push

                    │

                    ▼

          GitHub Repository

                    │

                    ▼

          GitHub Actions CI

      ┌─────────────┴─────────────┐

      ▼                           ▼

 Gitleaks Scan             Docker Build

                                    │

                                    ▼

                              Trivy Scan

                                    │

                            Security Gate

                             PASS / FAIL
```

---

# 🚀 Project Roadmap

| Phase | Description | Status |
|---------|-------------|:------:|
| Phase 1 | Project Initialization | ✅ Completed |
| Phase 2 | Dockerize Flask Application | ✅ Completed |
| Phase 3 | Harden Docker Container | ✅ Completed |
| Phase 4 | Push Project to GitHub | ✅ Completed |
| Phase 5 | GitHub Actions Workflow | ✅ Completed |
| Phase 6 | Secret Scanning with Gitleaks | ✅ Completed |
| Phase 7 | Vulnerability Scanning with Trivy | ⏳ Pending |
| Phase 8 | Security Gates | ⏳ Pending |
| Phase 9 | Pipeline Validation | ⏳ Pending |
| Phase 10 | Documentation & Finalization | ⏳ Pending |

---

# 📚 DevSecOps Concepts Covered

This project focuses on implementing the following DevSecOps concepts:

- Continuous Integration (CI)
- Shift Left Security
- Security Gates
- Secret Detection
- Container Security
- Vulnerability Management
- Least Privilege
- Docker Security

---

# 📈 Future Improvements

After completing this introductory project, future enhancements may include:

- SonarQube (SAST)
- pip-audit (SCA)
- OWASP ZAP (DAST)
- Jenkins Pipeline
- Kubernetes Deployment
- Kyverno Policies
- HashiCorp Vault
- AWS Deployment
- Terraform Integration

---

# 🤝 Acknowledgements

This project is part of my hands-on DevSecOps learning journey, focusing on understanding how security tools integrate into modern CI/CD pipelines through practical implementation.
