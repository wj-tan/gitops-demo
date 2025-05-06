# GitOps-based 3-Tier Application Deployment with Argo CD


## Argo CD Installation on Kubernetes

`kubectl create namespace argocd`

`kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml`

`kubectl port-forward svc/argocd-server -n argocd 8080:443`

`kubectl get secret -n argocd argocd-initial-admin-secret -o yaml`
