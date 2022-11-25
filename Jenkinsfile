pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Tejdeep2003/jenkins.git'
            }
        }
      stage('Provide permissions'){
        steps{
             sh "chmod u+x subtraction.py"
             sh "chmod u+x test.py test1.py test2.py test3.py test4.py test5.py"
        }
      }
        stage('Build Code') {
            steps {
                sh "./subtraction.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "./test.py"
            }
        }
    } 
}
