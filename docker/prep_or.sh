apt-get -y update
apt install -y clangd-20
cd /OpenROAD
git apply /opt/ord.patch
./etc/DependencyInstaller.sh -all
./etc/Build.sh