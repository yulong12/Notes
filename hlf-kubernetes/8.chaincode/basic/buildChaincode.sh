#!/bin/bash

echo "========build chaincode========="
docker build -t default-route-openshift-image-registry.apps.bj-prod-14.luban.cdl.ibm.com/fabric/tcmpcc:v1.0 .

echo "========login luban========="
docker login -u $(oc whoami) -p $(oc whoami -t) default-route-openshift-image-registry.apps.bj-prod-14.luban.cdl.ibm.com

echo "========push chaincode image========="
docker push default-route-openshift-image-registry.apps.bj-prod-14.luban.cdl.ibm.com/fabric/tcmpcc:v1.0
