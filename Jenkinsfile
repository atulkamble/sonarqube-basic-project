pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/atulkamble/sonarqube-basic-project'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'MySonarScanner'

                    withSonarQubeEnv('MySonar') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=sonarqube-basic-project \
                            -Dsonar.sources=.
                        """
                    }
                }
            }
        }
    }
}