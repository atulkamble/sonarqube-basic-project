pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/atulkamble/sonarqube-project'
            }
        }

        stage('Install Test Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --user pytest pytest-cov
                '''
            }
        }

        stage('Run Tests and Coverage') {
            steps {
                sh '''
                    python3 -m pytest \
                    --cov=app \
                    --cov-report=xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'mySonar'

                    withSonarQubeEnv('MySonar') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=sonarqube-basic-project \
                            -Dsonar.projectName="Python Basic Project" \
                            -Dsonar.projectVersion=1.0 \
                            -Dsonar.sources=. \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }
    }
}
