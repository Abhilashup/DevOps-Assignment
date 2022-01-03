pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                bat 'python calc.py'
            }
        }
        stage('test') {
            steps {
                bat 'python test_calc.py'
            }
        }
    }
}
