pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'calc.py'
            }
        }
        stage('test') {
            steps {
                sh 'test_calc.py'
            }
        }
    }
}
