

mkdir /mnt/123/zipped
mkdir /mnt/123/unzipped

cp  /mnt/census/census_2000/datasets/Summary_File_1/*/*01_uf1.zip  /mnt/123/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*02_uf3.zip  /mnt/123/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*03_uf3.zip  /mnt/123/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*05_uf3.zip  /mnt/123/zipped       
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*06_uf3.zip  /mnt/123/zipped

unzip "/mnt/123/zipped/*.zip" -d /mnt/123/unzipped
cat /mnt/123/unzipped/*geo* > /mnt/123/supergeo.txt
cat /mnt/123/unzipped/*0*.u* > ~/mnt/123/superfile.txt