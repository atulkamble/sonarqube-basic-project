```
// jenkins server 

git clone https://github.com/atulkamble/ec2-jenkins
terraform init 
terraform plan 
terraform apply 

ssh >>
server-ip:9000

// sonarqube manual installation 

https://github.com/atulkamble/ec2-sonarqube

// sonarqube project 

1. login to sonarqube server 
2. install sonar-scanner cli as well in server

cd /opt
sudo wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-8.1.0.6389.zip
sudo unzip sonar-scanner-cli-8.1.0.6389.zip
sudo mv sonar-scanner-8.1.0.6389/ sonar-scanner
echo 'export PATH=$PATH:/opt/sonar-scanner/bin' | sudo tee /etc/profile.d/sonar-scanner.sh 
source /etc/profile.d/sonar-scanner.sh
sonar-scanner -h
sonar-scanner -v

3. create project sonarqube-basic-project 
4. create token and notedown it 

sqp_3583b20d8c11acd28d6b7c7a8ca1c3d367e57c29

5. >> create local project on sonarqube server

git clone https://github.com/atulkamble/sonarqube-basic-project
cd sonarqube-basic-project
git checkout test 

6. scan code via following command 

sonar-scanner \
  -Dsonar.projectKey=sonarqube-basic-project \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://3.81.167.42:9000 \
  -Dsonar.login=sqp_3583b20d8c11acd28d6b7c7a8ca1c3d367e57c29

7. // run pipeline with github

// fork and clone project, maintain project code from your side
https://github.com/atulkamble/sonarqube-basic-project

8. // Pipeline Run and add following settings

Manage Jenkins → Tools → SonarQube Scanner installations
Name: mySonar
☑ Install automatically

Then separately configure the SonarQube server connection:
Manage Jenkins → System → SonarQube installations

Name: MySonar
Server URL: http://3.82.58.85:9000
Server authentication token: >> Add Following Settings 

Add Credentials → Select a type of credential

Kind:        Secret text
Scope:       Global
Secret:      sqp_3583b20d8c11acd28d6b7c7a8ca1c3d367e57c29
ID:          sonar-token
Description: SonarQube Authentication Token


def scannerHome = tool 'mySonar'

withSonarQubeEnv('MySonar') {
    sh """
        ${scannerHome}/bin/sonar-scanner \
        -Dsonar.projectKey=sonarqube-basic-project \
        -Dsonar.sources=.
    """
}



```

