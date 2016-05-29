‹
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
echo "made vector json dict"

cat /mnt/volume/unzipped/*0*.u* > /mnt/volume/superfile.txt
echo "made superfile"

python /home/ec2-user/123project/cleaners/correct_complete_vectors.py \
    -r emr /mnt/volume/superfile --index=/mnt/volume/new_json_dict.json \
    > /mnt/volume/raw_vectors.txt
echo "made raw vectors"


python /home/ec2-user/123project/cleaners/generate_sample_stats.py \
    '/mnt/volume/raw_vectors.txt' '/mnt/volume/vectors.txt' \
    '/mnt/volume/avgs.txt' '/mnt/volume/stds.txt'
echo "made final vectors, averages and stds"

python /home/ec2-user/123project/analyzers/pairs_mapreduce.py \
    /mnt/volume/vectors --vectors=/mnt/volume/vectors \
    > /mnt/volume/allpairs.txt
echo "made all pairs"

python pairstoneighbors.py /mnt/volume/allpairs.txt \
    /mnt/volume/neighbors.json /mnt/volume/allplaces.txt
echo "made neighbordict.json and allplaces.txt"


python /home/ec2-user/123project/analyzers/homogenous_MR.py \
    -r emr /mnt/volume/allplaces.txt \
    --vectors=/mnt/volume/new_json_dict.json \
    --neighbors=/mnt/volume/neighbordict.json \
    > homogenousareas.txt
echo "made homogenous areas"

python /home/ec2-user/123project/analyzers/surfacearea.py \
    -r emr /mnt/volume/homogenousareas.txt \
    --n=10 \
    > surfaceareas.txt
echo " found top 10 homogenous areas"



    