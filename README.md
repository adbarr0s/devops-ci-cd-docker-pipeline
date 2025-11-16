# DevOps CI/CD Docker Pipeline

Este repositório demonstra um pipeline completo de **CI/CD moderno** usando:

- **FastAPI** como aplicação de exemplo
- **Docker (multi-stage build)** para containerização
- **GitHub Actions** para CI/CD
- **Pytest** para testes automatizados

O objetivo é demostrar um **exemplo profissional de práticas DevOps**, incluindo:
- Integração Contínua (build + testes)
- Entrega Contínua (build + push de imagem Docker)
- Padronização de ambiente via containers

---

## 🧱 Arquitetura do Projeto

```text
devops-ci-cd-docker-pipeline/
│
├── app/
│   ├── main.py              # Aplicação FastAPI
│   ├── requirements.txt     # Dependências Python
│   └── tests/
│       └── test_app.py      # Testes automatizados (pytest)
│
├── Dockerfile               # Multi-stage Docker build
│
└── .github/
    └── workflows/
        └── ci-cd.yml        # Pipeline CI/CD com GitHub Actions
