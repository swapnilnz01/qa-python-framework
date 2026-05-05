pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    playwright install --with-deps chromium
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    . venv/bin/activate
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