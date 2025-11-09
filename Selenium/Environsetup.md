# Selenium Java: Environment Setup

## Libraries Required
Selenium, Cucumber, Maven

---

## Update System
Update and upgrade your system using: `sudo apt update && sudo apt upgrade -y`

---

## Install Java (OpenJDK)
Install the default Java Development Kit using: `sudo apt install default-jdk -y`  
Verify installation by running: `java -version` and `javac -version`  

If you need a specific Java version, for example Java 17, install it using: `sudo apt install openjdk-17-jdk -y`

---

## Set JAVA_HOME
Find the Java installation path using: `update-java-alternatives -l`  
Open your profile file with `nano ~/.bashrc` or `nano ~/.zshrc`  
Add or update the following lines to set JAVA_HOME:  
`export JAVA_HOME="/usr/lib/jvm/java-1.21.0-openjdk-amd64"`  
`export PATH="$JAVA_HOME/bin:$PATH"`  
Save and reload your profile using `source ~/.bashrc` or `source ~/.zshrc`

---

## Configure Default Java Version (if multiple versions installed)
Run `sudo update-alternatives --config java` and `sudo update-alternatives --config javac` to select the default version

---

## Confirm Setup
Check JAVA_HOME and Java version using: `echo $JAVA_HOME` and `java -version`

---

## Download and Install Eclipse IDE on Linux
Eclipse IDE is an open-source, extensible, and cross-platform development environment. It is used to develop, compile, and execute projects, and provides a robust code editor with syntax highlighting, autocompletion, and code formatting.

**Installation Steps:**  
1. Navigate to downloads: `cd ~/Downloads`  
2. Download Eclipse installer: `wget -c -O eclipse-inst-jre-linux64.tar.gz "https://download.eclipse.org/oomph/products/latest/eclipse-inst-jre-linux64.tar.gz"`  
3. Extract the downloaded file: `tar -xzf eclipse-inst-jre-linux64.tar.gz`  
4. Navigate to the installer directory: `cd eclipse-installer`  
5. Run the installer: `./eclipse-inst`
