# Selenium Java: Environment Setup

## Install and Configure Java on Linux Machine

**Libraries required:** Selenium, Cucumber, and Maven

1. Update System
sudo apt update && sudo apt upgrade -y

2. Install Java (OpenJDK)
sudo apt install default-jdk -y
**Verify installation:**
java -version
javac -version
**If you need a specific Java version (e.g., Java 17):**
sudo apt install openjdk-17-jdk -y

3. Set JAVA_HOME
**Find the installation path:**
update-java-alternatives -l
**Copy the path, then open your profile file:**
nano ~/.bashrc
# or
nano ~/.zshrc
**Add/create bash profile:**
export JAVA_HOME="/usr/lib/jvm/java-1.21.0-openjdk-amd64"
export PATH="$JAVA_HOME/bin:$PATH"
**Save and reload:**
source ~/.bashrc
# or
source ~/.zshrc

4. Configure Default Java Version (If multiple versions installed)
sudo update-alternatives --config java
sudo update-alternatives --config javac

5. Confirm Setup
echo $JAVA_HOME
java -version

**Download and Install Eclipse IDE on Linux**

Eclipse IDE (Integrated Development Environment)
1. Open-source, extensible, and cross-platform (Windows, Linux, macOS)
2. Used to develop, compile, and execute projects
3. Provides a robust code editor with syntax highlighting, autocompletion, and code formatting

**Steps to Install:**
-> cd ~/Downloads
-> wget -c -O eclipse-inst-jre-linux64.tar.gz "https://download.eclipse.org/oomph/products/latest/eclipse-inst-jre-linux64.tar.gz"
-> tar -xzf eclipse-inst-jre-linux64.tar.gz
-> cd eclipse-installer    # or the directory created after extraction
-> ./eclipse-inst
