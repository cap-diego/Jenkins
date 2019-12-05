pipeline {
  agent any
  tools {
    nodejs 'node-13.3.0'
  }
  options {
    timeout(time:2, unit: 'MINUTES')
  }
  stages {
    stage("Run first time"){
      steps {
        sh 'cd src && npm i'
      }
   }
    stage("Run second time"){
      steps {
        sh 'cd src && npm t'
      }
    }

  }
}