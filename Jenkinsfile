pipeline{
agent any
    stages{
        stage('clone'){
            steps{
                echo "Not cloning"
            }
        }
        stage('Build'){
            steps{
                chmod u+x Prog1.py
                python3 Prog1.py
            }
        }
        stage('Test'){
            steps{
                chmod u+x Test.py
                python3 Test.py
            }
        }
    }
}
