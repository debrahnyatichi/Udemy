**Selenium Java:Environment Setup**
**Install and Configure Java on Linux Machine**
Libraries required: Selenium, cucumber and maven
1. Update System
sudo apt update && sudo apt upgrade -y
2. Install Java (OpenJDK)
sudo apt install default-jdk -y
**Verify:**
java -version
javac -version
**If you need a specific Java version, for example Java 17:**
sudo apt install openjdk-17-jdk -y
3. Set JAVA_HOME
**Find the installation path:**
update-java-alternatives -l
**Copy the path, then open your profile file:**
nano ~/.bashrc or ~/.zshrc
**Add/create bash profile:**
export JAVA_HOME="/usr/lib/jvm/java-1.21.0-openjdk-amd64"
export PATH="$JAVA_HOME/bin:$PATH"
**Save and reload:**
source ~/.bashrc OR
source ~/.zshrc
4. Configure Default Java Version (If multiple versions installed)
sudo update-alternatives --config java
sudo update-alternatives --config javac
5. Confirm
echo $JAVA_HOME
java -version

**Download and Install IDE Eclipse on Linux**
EclipseIDE(Intergrated Development Environment): it is an open source extensible, cross-platform development tool used for java development
Eclipse IDE: 
Is used to develop, compile and execute the code/project
It is designed to work seamlessly on diff OS: win,linux and macOS
It provides a robust coe editor with features like syntax highlighting,autocompletion, code formatting

cd ~/Downloads
wget -c -O eclipse-inst-jre-linux64.tar.gz \
"https://download.eclipse.org/oomph/products/latest/eclipse-inst-jre-linux64.tar.gz"
tar -xzf eclipse-inst-jre-linux64.tar.gz
cd eclipse-installer    # or similar dir created
./eclipse-inst

