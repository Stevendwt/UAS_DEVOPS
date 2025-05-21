pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-flask-app"
        CONTAINER_NAME = "flask-login"
        PORT = "5001"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'development', url: 'https://github.com/Stevendwt/UAS_DEVOPS.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Stop Previous Container') {
            steps {
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                    docker run -d --name $CONTAINER_NAME -p $PORT:5001 $IMAGE_NAME
                '''
            }
        }
    }
}
