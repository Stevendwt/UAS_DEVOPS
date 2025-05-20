pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Stevendwt/UAS_DEVOPS.git'
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
