pipeline { 
    agent any

    environment {
        IMAGE_NAME = "sas-location-inference-service"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\pip.exe install --upgrade pip'
                bat '.\\venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\pytest.exe tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo "Build and tests successful!"
        }
        failure {
            echo "Build or tests failed."
        }
    }
}
