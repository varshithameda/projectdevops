pipeline {
    agent any

    environment {
        APP_NAME = "ecommerce-demo"
        DOCKER_IMAGE = "srivarshithameda/week12:ecommercedemoapp"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat "docker build -t %APP_NAME%:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u srivarshithameda -p #Varshitha2344'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Tag and Push Image to Docker Hub..."
                bat "docker tag %APP_NAME%:v1 %DOCKER_IMAGE%"
                bat "docker push %DOCKER_IMAGE%"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                bat '''
                set KUBECONFIG=C:\\Users\\abhi\\.kube\\config
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment Successful!"
        }
        failure {
            echo "❌ Deployment Failed!"
        }
    }
}
