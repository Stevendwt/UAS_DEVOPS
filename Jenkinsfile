pipeline {
    agent {
        docker {
            image 'node:16'
            args '-u root:root'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'development', url: 'https://github.com/Stevendwt/UAS_DEVOPS.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'npm test'
            }
        }
    }
}
