
cp  /mnt/census/census_2000/datasets/Summary_File_1/*/*01_uf1.zip  ~/thepile                   \
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*02_uf3.zip  ~/thepile             
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*03_uf3.zip  ~/thepile        
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*05_uf3.zip  ~/thepile        
cp  /mnt/census/census_2000/datasets/Summary_File_3/*/*06_uf3.zip  ~/thepile

unzip "~/thepile/*.zip"
cat *~/thepile/*.u* > ~/thepile/superfile.txt