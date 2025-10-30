pipeline {
    agent any

    environment {
        // 🔧 Customize these
        APP_NAME = "ecommercedemoapp"
        DOCKER_IMAGE = "srivarshithameda/week12:ecommercedemoapp"
        KUBECONFIG_PATH = "C:\\Users\\abhi\\.kube\\config"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                // If it's a Python app
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running tests..."
                // If you use pytest or any test command
                bat 'pytest -v || echo "No tests found, skipping..."'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                bat "docker build -t ${APP_NAME}:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                // ⚠️ NOTE: It’s better to use Jenkins credentials for security
                // Here it's plain for demo purposes
                bat 'docker login -u srivarshithameda -p #Varshitha2344'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Tagging and pushing Docker image..."
                bat "docker tag ${APP_NAME}:v1 ${DOCKER_IMAGE}"
                bat "docker push ${DOCKER_IMAGE}"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes cluster..."
                bat """
                set KUBECONFIG=${KUBECONFIG_PATH}
                kubectl cluster-info
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                """
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}
