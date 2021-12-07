kubectl get pods -l run=inference -o yaml | grep podIP


kubectl get pods -l run=inference -o wide

inference-54c85c46d-8sh9f   2/2     Running   0          42s   10.36.0.1   node1   <none>           <none>
inference-54c85c46d-qhmdg   2/2     Running   0          42s   10.36.0.2   node1   <none>           <none>
inference-54c85c46d-xljmn   2/2     Running   0          42s   10.44.0.1   node2   <none>           <none>


curl 10.36.0.1:6666

curl 10.110.247.98:6666


openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /root/Mul_cloud/secrets/inference.key -out /root/Mul_cloud/secrets/inference.crt -subj "/CN=inference/O=inference"


cat /root/Mul_cloud/secrets/inference.key | base64
cat /root/Mul_cloud/secrets/inference.crt | base64



curl -k -H "Content-Type: application/json" -i -X POST --data '{"data":[1.0140032768249512, 1.0712705850601196, 0.9839876890182495, 1.3597276210784912, 0.005677420180290937, 1.0156164169311523, 1.5999584197998047, 0.2245749831199646]}' https://9.30.250.239:6666/inference/1ae32cd66761d98b9af0870a963ee459