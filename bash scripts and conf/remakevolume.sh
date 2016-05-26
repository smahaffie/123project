

mkdir /mnt/volume/zipped
mkdir /mnt/volume/unzipped

cp  /mnt/census/census_2000/datasets/Summary_File_1/*/*01_uf1.zip  /mnt/volume/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*02_uf3.zip  /mnt/volume/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*03_uf3.zip  /mnt/volume/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*05_uf3.zip  /mnt/volume/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*06_uf3.zip  /mnt/volume/zipped

unzip "/mnt/volume/zipped/*.zip" -d /mnt/123/unzipped
cat /mnt/volume/unzipped/*geo* > /mnt/123/supergeo.txt
cat /mnt/volume/unzipped/*0*.u* > ~/mnt/123/superfile.txt