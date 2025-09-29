apt-get -y update
cd /OpenROAD
./etc/DependencyInstaller.sh -all
./etc/Build.sh
apt install -y clangd-12