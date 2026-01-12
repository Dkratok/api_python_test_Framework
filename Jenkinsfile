pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run pytest') {
            steps {
                sh '''
                pytest ./tests --html=report.html --self-contained-html
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'report.html', fingerprint: true
                }
            }
        }
    }
}