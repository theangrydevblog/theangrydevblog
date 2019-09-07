#! /bin/bash

set -e

COMMIT_SHA1=$CIRCLE_SHA1

# We must export it so it's available for envsubst
export COMMIT_SHA1=$COMMIT_SHA1

envsubst <./.k8s/deployment.yml >./.k8s/deployment.yml.out
mv ./.k8s/deployment.yml.out ./.k8s/deployment.yml

echo "$KUBERNETES_CLUSTER_CERTIFICATE" | base64 --decode > cert.crt

./kubectl \
  --kubeconfig=/dev/null \
  --server=$KUBERNETES_SERVER \
  --certificate-authority=cert.crt \
  --token=$KUBERNETES_TOKEN \
  apply -f ./.k8s/
