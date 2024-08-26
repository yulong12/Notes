  stage('Scan Code'){
      agent{ label agentAutomation }
      environment{
        CONTRAST__API__URL='https://app.contrastsecurity.com/Contrast/api/sast'
        CONTRAST__API__USER_NAME='wangbjj@cn.ibm.com'
        CONTRAST__API__API_KEY='vgy5soZn15wnVPHH539pF8F7niofbl4N'
        CONTRAST__API__SERVICE_KEY='GTHWPVOHX2V86FCM'
        CONTRAST__API__ORGANIZATION='142bb017-de7e-4af7-b5b9-f0782aa6d369'
        CONTRAST_AUTH_TOKEN='d2FuZ2JqakBjbi5pYm0uY29tOkdUSFdQVk9IWDJWODZGQ00='
      }
      when { 
          anyOf {
            expression { params.IfAutomation == "ALL" || params.IfAutomation == 'SCAN_CODE' }
          }
      }
        steps{
          script{
                    dir(path: "${WORKSPACE}"){
                            sh(script: 'rm -rf ${WORKSPACE}/*', returnStdout: true)
                            checkout ([$class: 'GitSCM', branches: [[name: '*/main']],
                            doGenerateSubmoduleConfigurations: false, extensions: [], 
                            submoduleCfg: [],
                            userRemoteConfigs: [[credentialsId: 'automation_test_machine', url: 'git@github.ibm.com:ZLDA/zcdp_automationTest.git']]])
                            sh "chmod +x ${WORKSPACE}/shell_script/ui_Prepare.sh"
                            sh "sh ${WORKSPACE}/shell_script/ui_Prepare.sh ALL 'CSL005' ${BuildNo} No /u/510postGA ${WORKSPACE}"
                            sh "ansible-playbook -i inventories ${WORKSPACE}/ansible_script/mount.yaml"
 						                sh "ansible-playbook -i inventories ${WORKSPACE}/ansible_script/downLoadJar.yaml" 
                            sh "mkdir -p SAST/zipJars"   
                            sh "cd ${WORKSPACE}/SAST/jars ; zip -qq -r ${WORKSPACE}/SAST/zipJars/cdp.zip ./*"
                            sh "java -jar ${WORKSPACE}/tool/sast-local-scan-runner-1.0.9.jar ${WORKSPACE}/SAST/zipJars/cdp.zip --project-name ${JOB_NAME}-${BUILD_ID} --label ${CONTRAST__API__USER_NAME} -r \"IBM Z Common Data Provider\""
                            sleep 180

                    }
            
          }
        }
        post{
              always{
                    script{
                            echo "Generate Report"
							api_1 = """
							curl -s \
							-X GET \
							${CONTRAST__API__URL}/v1/organizations/${CONTRAST__API__ORGANIZATION}/projects?name=${JOB_NAME}-${BUILD_ID} \
							-H 'Authorization: '${CONTRAST_AUTH_TOKEN}'' \
							-H 'API-Key: '${CONTRAST__API__API_KEY}''
							"""
							output_api_1 = sh(script: api_1, returnStdout: true)
							writeFile(file:'scan_report.json', text:output_api_1)

							filterCmd = """
										jq -c '.content | .[] | select(.name == "${JOB_NAME}-${BUILD_ID}") | .id' scan_report.json
										"""
							projectid = sh(script: filterCmd, returnStdout: true).trim()

							api_2 = """
							curl -s \
							-X GET \
							${CONTRAST__API__URL}/organizations/${CONTRAST__API__ORGANIZATION}/projects/${projectid}/results/csv \
							-H 'Authorization: '${CONTRAST_AUTH_TOKEN}'' \
							-H 'API-Key: '${CONTRAST__API__API_KEY}'' \
							-H 'Accept: application/json'
							"""
							output_api_2 = sh(script: api_2, returnStdout: true).trim()
							writeFile(file:"${JOB_NAME}-${BUILD_ID}.csv", text:output_api_2)
              sh "ansible-playbook -i inventories ${WORKSPACE}/ansible_script/unmount.yaml" 
              sh "ansible-playbook -i inventories ${WORKSPACE}/ansible_script/delete_mount_dir.yaml" 

                    }
                archiveArtifacts(artifacts: "${JOB_NAME}-${BUILD_ID}.csv", followSymlinks: false)
                }
        }
    }