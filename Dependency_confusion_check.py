for i in `cat org.txt`;do python3.11 scripter3.py $i;done >> scripterout.txt

cat scripterout.txt | grep Requirements | cut -d ' ' -f 3- | sed 's/github.com/raw.githubusercontent.com/g' | sed 's/\/blob//g' >> scripterout2.txt

for i in `cat scripterout2.txt` ;do echo $i && printf "\n" && curl -s $i && printf "\n";done >> temp2.txt

cat temp2.txt | cut -d '#' -f -1| cut -d '=' -f -1 |cut -d '>' -f -1 | cut -d ';' -f -1 | cut -d '~' -f -1 | cut -d '(' -f -1 | cut -d '<' -f -1| cut -d '!' -f -1|grep -iv 'git+' |grep -iv 'https:'|sed 's/ *$//' | grep -v -- '-e' |grep -v '^$' >> temp3.txt

for i in `cat temp3.txt`; do python3.11 packagecheck2.py $i; done

cat non_existent_packages.txt | grep -v '^\.$' | grep -v -- '-e' > non_existent_packages2.txt

chmod 777 hiren.sh

./hiren.sh