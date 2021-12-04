i=0

elapsedTime=()
while [ $i -lt 20 ]
do
    start_time=$(date +%s.%3N)
    spark-3.2.0-bin-hadoop3.2/bin/spark-submit --master spark://spark-master-svc:7077 --properties-file spark-3.2.0-bin-hadoop3.2/conf/spark-driver.conf energy-counter.py    
    end_time=$(date +%s.%3N)
    elapsedTime+=( $(echo "scale=3; $end_time - $start_time" | bc) )
    i=`expr $i + 1`
done

printf '%s\n' "${elapsedTime[@]}"