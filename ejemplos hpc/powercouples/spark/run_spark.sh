#!/bin/bash
# 
# Spark 2.0 Slurm submision script
#
# Deploy master and workers, then submit the python script
#
# 2016 (c) Juan Carlos Maureira
# Center for Mathematical Modeling
# University of Chile

# make the spark module available
module use -a $HOME/modulefiles
module load spark
module load python/2.7.10

NUM_WORKERS=2
CORES_PER_WORKER=20

if [ "$1" == "deploy" ]; then
    # deploy spark workers on nodes

    MASTER=$2
    HOST=`hostname -a`
    echo "starting slave at $HOST"
    $SPARK_HOME/sbin/start-slave.sh --cores $CORES_PER_WORKER spark://$MASTER:7077  

    tail -f /dev/null
else
    # main routine

    MASTER=`hostname -a`
    echo "Using as master $MASTER"
    $SPARK_HOME/sbin/start-master.sh 

    srun --exclusive -n $NUM_WORKERS -c $CORES_PER_WORKER -J spark $0 deploy $MASTER &

    sleep 10

    spark-submit --master spark://$MASTER:7077 $@

    # clean up
    scancel --name spark 
    $SPARK_HOME/sbin/stop-master.sh 
    echo "done"
fi

