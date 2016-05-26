
mkdir /mnt/volume/zipped
mkdir /mnt/volume/unzipped
echo "made zipped, unzipped"

echo "copying summary files"
cp  /mnt/census/census_2000/datasets/Summary_File_1/*/*01_uf1.zip  /mnt/volume/zipped  
echo "done table 1"     
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*02_uf3.zip  /mnt/volume/zipped 
echo "done table 2"      
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*03_uf3.zip  /mnt/volume/zipped 
echo "done table 3"
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*05_uf3.zip  /mnt/volume/zipped 
echo "done table 5"
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*06_uf3.zip  /mnt/volume/zipped
echo "done table 6"

rm /mnt/volume/unzipped/pr*
rm /mnt/volume/unzipped/us*
rm /mnt/volume/unzipped/dc*
echo "removed PR, US, DC"

unzip "/mnt/volume/zipped/*.zip" -d /mnt/123/unzipped
echo "unzipped everything"

cat /mnt/volume/unzipped/*geo* > /mnt/123/supergeo.txt
echo " super geo made"
cat /mnt/volume/unzipped/*0*.u* > ~/mnt/123/superfile.txt
echo "makde superfile"
