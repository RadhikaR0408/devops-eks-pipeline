# DevOps Pipeline on AWS (Cost-Optimized EKS)

## Project Overview

This project demonstrates a **DevOps pipeline** using modern cloud-native tools, designed with **cost optimization** and **real-world best practices** in mind.

The infrastructure is provisioned temporarily for demonstration purposes and **fully destroyed after validation** to avoid unnecessary AWS costs.

---

## Architecture

**Core components:**

* **Application**: Containerized app (Docker)
* **CI/CD**: GitHub Actions
* **Container Registry**: Amazon ECR
* **Infrastructure as Code**: Terraform
* **Orchestration**: Amazon EKS (minimal node group)
* **Monitoring**: Prometheus & Grafana (Helm)

---

## CI/CD Workflow

1. Code pushed to GitHub
2. GitHub Actions pipeline triggered
3. Docker image built
4. Image pushed to Amazon ECR
5. Kubernetes manifests used to deploy app on EKS

---

## Deployment Steps (High-Level)

1. **CI/CD**

   * Push code to GitHub
   * GitHub Actions builds and pushes Docker image to ECR

2. **Infrastructure Provisioning**

   ```bash
   terraform init
   terraform apply
   ```

3. **Kubernetes Deployment**

   ```bash
   kubectl apply -f app/k8s/
   ```

4. **Monitoring Setup**

   ```bash
   helm install monitoring prometheus-community/kube-prometheus-stack \
     --namespace monitoring \
     --create-namespace
   ```

5. **Access Grafana**

   ```bash
   kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80
   ```

---

## Observability

* Prometheus collects cluster and application metrics
* Grafana provides visualization dashboards
* Dashboards verified during live runtime

---

## Cost Optimization Strategy

* Minimal EKS node group (single small instance)
* Short-lived cluster (created only for demo)
* Full teardown after validation

```bash
terraform destroy
```

---

## Key Takeaways

* Infrastructure as Code best practices
* Secure CI/CD pipeline
* Kubernetes deployment workflows
* Monitoring and observability
* Cloud cost discipline

---

## Cleanup (Mandatory)

```bash
terraform destroy
```

---

**Author:** Radhika
