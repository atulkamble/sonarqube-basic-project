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
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=sonarqube-basic-project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://3.81.167.42:9000 \
                        -Dsonar.login=sqp_3583b20d8c11acd28d6b7c7a8ca1c3d367e57c29
                    '''
                }
            }
        }
    }
}