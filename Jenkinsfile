pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv env
                    . env/bin/activate
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    . env/bin/activate
                    pytest tests/api/ -v --html=reports/report.html --self-contained-html
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportName: 'Pytest HTML Report',
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ])
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed. Check the report.'
        }
    }
}