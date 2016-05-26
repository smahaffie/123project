
mkdir /mnt/volume/zipped
mkdir /mnt/volume/unzipped
mkdir /mnt/volume/zippedgeo
mkdir /mnt/volume/unzippedgeo
echo "made zipped, unzipped, zippedgeo"

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

cp /mnt/census/census_2000/datasets/Summary_File_1/*/*geo* /mnt/volume/zippedgeo
cp /mnt/census/census_2000/datasets/Summary_File_3/*/*geo* /mnt/volume/zippedgeo
echo "copied geo files"

rm /mnt/volume/zip*/pr*
rm /mnt/volume/zip*/us*
rm /mnt/volume/zip*/dc*
echo "removed PR, US, DC"

unzip "/mnt/volume/zipped/*" -d /mnt/volume/unzipped
unzip "/mnt/volume/zippedgeo/*" -d /mnt/unzippedgeo
echo "unzipped everything"

cd /mnt/volume/unzippedgeo
python /home/ec2-user/123project/cleaners/header_with_lon_lat.py
echo "made csvs from geos"

python /home/ec2-user/123project/correct_make_json.py
mv new_json_dict.json ..
echo "made json dict"

cat /mnt/volume/unzipped/*0*.u* > /mnt/volume/superfile.txt
echo "made superfile"

python /home/ec2-user/123project/cleaners/correct_complete_vectors.py \
    -r emr /mnt/volume/superfile --index=new_json_dict




