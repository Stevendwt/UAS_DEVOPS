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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    PYTHONPATH=. pytest
                '''
            }
        }

        stage('Deploy to Local') {
            steps {
                sh '''
                    # Hentikan aplikasi jika sedang berjalan
                    pkill -f "venv/bin/python app.py" || true

                    # Aktifkan environment dan jalankan ulang
                    nohup venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
