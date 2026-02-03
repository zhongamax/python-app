helm upgrade --install release-v2 ./helm \
  --namespace catalyst \
  --create-namespace \
  --wait \
  --timeout 5m