
sudo apt install  https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && 
sudo apt install mesa-libOSMesa-devel gnu-free-sans-fonts wqy-zenhei-fonts
echo 'install chromedriver'
wget http://npm.taobao.org/mirrors/chromedriver/2.41/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/
echo  'changemod'
sudo chmod +x /usr/bin/chromedriver

echo 'install pyPackageSite'
sudo pip install -r piplist.txt

