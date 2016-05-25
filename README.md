Some Dask bench on Cori
===
Interactive session, realtime queue, exclusive access: `salloc -N 1 --exclusive -p realtime <args>`

Test programs
---
- Pandas: Read CSV file (1.4GB) and calculate the mean, `data.csv` is available via `wget http://portal.nersc.gov/project/mlhub/data_bench.csv`
- Numpy: Generate random array

Regular env on Cori
---

```sh
module load python
module load virtualenv
DBENCH_PATH=$HOME/dask_bench
virtualenv --system-site-packages $DBENCH_PATH/.venv ; cd $DBENCH_PATH
source $DBENCH_PATH/.venv/bin/activate
wget http://portal.nersc.gov/project/mlhub/data_bench.csv -0 $DBENCH_PATH/data_bench.csv
git clone foo
(time python $DBENCH_PATH/dbench/bench/regular/<test_code>) &> <test_code>.log
```

Vanilla Anaconda distro env
---

```sh
DBENCH_PATH=$HOME/dask_bench
mkdir -p $DBENCH_PATH/downloads
wget -0 $DBENCH_PATH/downloads/Anaconda2-4.0.0-Linux-x86_64.sh http://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh
bash $DBENCH_PATH/downloads/Anaconda2-4.0.0-Linux-x86_64.sh -b -p $DBENCH_PATH/.anaconda2
export PATH=$DBENCH_PATH/.anaconda2/bin:$PATH ; cd $DBENCH_PATH
wget http://portal.nersc.gov/project/mlhub/data_bench.csv -0 $DBENCH_PATH/data_bench.csv
git clone foo
(time python $DBENCH_PATH/dbench/bench/dask/<test_code>) &> <test_code>.log
```

Results
---
- Pandas: 0m6.776s (Dask) vs. 0m19.367s (regular)
- Numpy: (Dask) vs. (regular)


