pipeline {  
    environment {
    registry = "abhilashup/calculator"
    registryCredential = 'dockerhub'
  }  
  agent any  
  stages {
    stage('Build') {
      steps{
        script {
          docker.build registry + ":latest"
        }
      }
    }
    stage('Test'){
        steps {
            bat 'python test_calc.py'
        }
    }
  }
}
