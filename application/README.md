Some video-doc-tutorials:
nginx ingress controller and simple web app: https://www.youtube.com/watch?v=ezX4D1ZK5mA

Helm chart url: https://github.com/kubernetes/ingress-nginx/tree/main/charts/ingress-nginx

Commands to install:
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install hacktoberfestcoruna 
helm install --namespace hacktoberfest hacktoberfestcoruna ingress-nginx/ingress-nginx -f ingress-nginx/ingress-nginx-values.yaml


#testing aks app 
http//4.175.117.127/
Load balancer: 4.175.117.127 Dns: hacktoberfestcoruna.westeurope.cloudapp.azure.com

http://hacktoberfestcoruna.westeurope.cloudapp.azure.com/