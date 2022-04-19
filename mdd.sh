#!/bin/bash
wget https://www.dropbox.com/s/c9o2ouce2t1zfah/Webs.txt
cat Webs.txt |grep /2020 > 2020
cat 2020 |awk '{print $3}' > links
cat links |grep /2020 |grep -e 202009 -e 202010 -e 202011 -e 202012 > trimestr4
cat trimestr4 |grep mentions > mentions
cat trimestr4 |grep export > export
cat trimestr4 |grep gkg > gkg
mkdir iMENTIONS
mkdir iEXPORTS
mkdir iGKG
mkdir iMENTIONS/SEP2020
mkdir iMENTIONS/OCT2020
mkdir iMENTIONS/NOV2020
mkdir iMENTIONS/DIC2020
mkdir iEXPORTS/SEP2020
mkdir iEXPORTS/OCT2020
mkdir iEXPORTS/NOV2020
mkdir iEXPORTS/DIC2020
mkdir iGKG/SEP2020
mkdir iGKG/OCT2020
mkdir iGKG/NOV2020
mkdir iGKG/DIC2020
cat mentions |grep /202009 > /mnt/f/repositorios/hdinsight/iMENTIONS/SEP2020/ment_202009
cat mentions |grep /202010 > /mnt/f/repositorios/hdinsight/iMENTIONS/OCT2020/ment_202010
cat mentions |grep /202011 > /mnt/f/repositorios/hdinsight/iMENTIONS/NOV2020/ment_202011
cat mentions |grep /202012 > /mnt/f/repositorios/hdinsight/iMENTIONS/DIC2020/ment_202012
cat export |grep /202009 > /mnt/f/repositorios/hdinsight/iEXPORTScd/SEP2020/export_202009
cat export |grep /202010 > /mnt/f/repositorios/hdinsight/iEXPORTScd/OCT2020/export_202010
cat export |grep /202011 > /mnt/f/repositorios/hdinsight/iEXPORTScd/NOV2020/export_202011
cat export |grep /202012 > /mnt/f/repositorios/hdinsight/iEXPORTScd/DIC2020/export_202012
cat gkg |grep /202009 > /mnt/f/repositorios/hdinsight/iGKG/SEP2020/gkg_202009
cat gkg |grep /202010 > /mnt/f/repositorios/hdinsight/iGKG/OCT2020/gkg_202010
cat gkg |grep /202011 > /mnt/f/repositorios/hdinsight/iGKG/NOV2020/gkg_202011
cat gkg |grep /202012 > /mnt/f/repositorios/hdinsight/iGKG/DIC2020/gkg_202012
cd /mnt/f/repositorios/hdinsight/iMENTIONS/SEP2020/
wget -i ment_202009
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iMENTIONS/OCT2020
wget -i ment_202010
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iMENTIONS/NOV2020
wget -i ment_202011
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iMENTIONS/DIC2020
wget -i ment_202012
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iEXPORTS/SEP2020
wget -i export_202009
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iEXPORTS/OCT2020
wget -i export_202010
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iEXPORTS/NOV2020
wget -i export_202011
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iEXPORTS/DIC2020
wget -i export_202012
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iGKG/SEP2020
wget -i gkg_202009
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iGKG/OCT2020
wget -i gkg_202010
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iGKG/NOV2020
wget -i gkg_202011
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/iGKG/DIC2020
wget -i gkg_202012
sudo unzip '*.zip'
sudo rm *.zip
cd /mnt/f/repositorios/hdinsight/
