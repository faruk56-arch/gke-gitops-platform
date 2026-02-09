# GKE Production GitOps Platform

Production-grade Kubernetes platform built on **Google Kubernetes Engine (GKE)** using GitOps principles.

## Stack
- GKE (Google Kubernetes Engine)
- ArgoCD (GitOps)
- Helm + Kustomize
- Prometheus + Grafana + Loki
- Argo Rollouts (Canary deployments)
- HPA + PodDisruptionBudget
- RBAC + NetworkPolicies
- CI/CD with GitHub Actions
- Python (FastAPI) application with Prometheus metrics

## Architecture
- Git is the single source of truth
- ArgoCD continuously reconciles cluster state
- CI builds images and updates GitOps manifests
- Canary deployments validated via Prometheus metrics

## Environments
- dev
- staging
- prod

## Highlights
- Zero-downtime deployments
- Automated rollbacks on failed canary analysis
- Secure-by-default networking
- Full observability stack

## Author
Faruk Momin – DevOps / Cloud Engineer
