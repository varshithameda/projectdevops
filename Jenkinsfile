pipeline {
    agent any

    environment {
        APP_NAME = "project"                                   // your app name
        DOCKER_IMAGE = "srivarshithameda/ecommerce:latest"     // your Docker Hub image
    }

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image for ${APP_NAME}"
                bat "docker build -t ${APP_NAME}:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub"
                bat 'docker login -u srivarshithameda -p #Varshitha2344'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub"
                bat "docker tag ${APP_NAME}:v1 ${DOCKER_IMAGE}"
                bat "docker push ${DOCKER_IMAGE}"
            }
        }

        stage('Deploy to Kubernetes') { 
            steps { 
                echo "Deploying ${APP_NAME} to Kubernetes cluster"

                bat '''
                set KUBECONFIG=C:\\Users\\abhi\\.kube\\config
                kubectl cluster-info
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            } 
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully! Application deployed on Kubernetes.'
        }
        failure {
            echo '❌ Pipeline failed. Please check the Jenkins logs for details.'
        }
    }
}
