pipeline {
  agent none
  stages {
    stage('stage1') {
      environment {
        key1 = 'value1'
        key2 = 'value2'
      }
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
        echo 'step5'
      }
    }
  }
  environment {
    k1 = 'v1'
    k2 = 'v2'
  }
}