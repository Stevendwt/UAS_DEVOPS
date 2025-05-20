pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'development', url: 'https://github.com/Stevendwt/UAS_DEVOPS.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
