pipeline {
  agent any
  
  stages {
    stage('Download Source Code') {
      steps {
        git branch: 'main', url: 'https://github.com/fullaware/asteroids.git' 
      }
    }
    
    stage('Scan') {
      steps {
                // Install trivy html template
                sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl'

                // Scan all vuln levels
                sh 'mkdir -p reports'
                sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --format template --template "@html.tpl" -o reports/python-scan.html ./'
                publishHTML target : [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'python-scan.html',
                    reportName: 'Trivy Python Scan',
                    reportTitles: 'Trivy Python Scan'
                ]

                // Scan again and fail on CRITICAL vulns
                sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --exit-code 1 --severity CRITICAL ./'

            }
    }
    stage('Build Docker Container') {
      steps {
        sh 'docker-compose build'
      }
    }
    
    stage('Scan Container App Image with Trivy') {
      steps {
        sh 'trivy image -f json -o app-results.json fullaware/asteroids-app'
      }
    }
     stage('Scan Container API Image with Trivy') {
      steps {
        sh 'trivy image -f json -o api-results.json fullaware/asteroids-api'
      }
    }
    
  }
  
  post {
    always {
      archiveArtifacts artifacts: '*.json'
    }
  }
}
