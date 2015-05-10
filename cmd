sudo apt-get update
sudo apt-get install -y git python-setuptools python-dev libffi-dev libssl-dev
sudo easy_install -U pip

git clone https://github.com/pOOOOOr/ccc_task_2.git
cd ccc_task_2
sudo pip install -r requirements.txt
sudo pip install requests[security] --upgrade

sudo pip install uwsgi
sudo apt-get install nginx

----------------------
./twt_restful_crawler.py >rest.log 2>&1 &
python get_tweets_streamer.py xin 0 >stream.log 2>&1 &
python get_tweets_streamer.py nikvi 1 >stream.log 2>&1 &
python get_tweets_streamer.py nikvi 2 >stream.log 2>&1 &
python get_tweets_streamer.py zoey 3 >stream.log 2>&1 &
python get_tweets_streamer.py jacky 4 >stream.log 2>&1 &