pipeline {
    agent any

    environment {
        PLAYWRIGHT_BROWSERS_PATH = '/root/.cache/ms-playwright'
    }

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
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v -n auto \
                        --html=reports/report.html \
                        --self-contained-html
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
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo '✅ All tests passed!'
        }
        failure {
            echo '❌ Build failed. Check the logs.'
        }
    }
}