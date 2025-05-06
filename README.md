# GitOps-based 3-Tier Application Deployment with Argo CD


## Argo CD Installation on Kubernetes

### Install Argo CD

`kubectl create namespace argocd`

`kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml`

### Port Forwarding

`kubectl port-forward svc/argocd-server -n argocd 8080:443`

### Retrieve admin password (decode with base64)

`kubectl get secret -n argocd argocd-initial-admin-secret -o yaml`
