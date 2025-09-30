apt-get -y update
apt install -y clangd-20
cd /OpenROAD
./etc/DependencyInstaller.sh -all
./etc/Build.sh