pipeline {
  agent any
  stages {
    stage('stage1') {
      parallel {
        stage('stage1') {
          steps {
            echo 'step1'
            echo 'step2'
            echo 'step3'
          }
        }
        stage('stage2') {
          steps {
            echo 'step4'
          }
        }
      }
    }
    stage('stage3') {
      steps {
        bat 'echo "step5"'
      }
    }
  }
}