#!/bin/bash
tar cfz code.tar.gz connection.json
tar cfz basic-org1.tgz code.tar.gz metadata.json
tar cfz basic-org2.tgz code.tar.gz metadata.json
tar cfz basic-org3.tgz code.tar.gz metadata.json
chmod 777 -R ./*