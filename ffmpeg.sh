#!/bin/bash
source /opt/sahibinden/system/scripts/ffmpeg-env.sh
cd /home/devops
wget http://ffmpeg.org/releases/ffmpeg-2.7.2.tar.bz2 && tar xvjf ffmpeg-2.7.2.tar.bz2 && cd ffmpeg-2.7.2/
apt-get remove -y  ffmpeg && apt-get autoremove -y && apt-get install -y deb-multimedia-keyring && apt-get install build-essential libmp3lame-dev libvorbis-dev libtheora-dev
echo "deb http://www.deb-multimedia.org stretch main  non-free" >> /etc/apt/sources.list && apt-get update
export TMPDIR=/hometmp-ffmpeg
mkdir $TMPDIR
./configure --enable-gpl --enable-version3 --enable-shared --enable-nonfree --enable-postproc --enable-libfaac --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libtheora --enable-libvorbis --enable-libx264  --enable-x11grab --extra-cflags="-I/usr/local/include" --extra-ldflags="-L/usr/local/lib"
make -j2 && make install
apt install -y ffmpeg
rm -rf ~/tmp-ffmpeg /home/devops/ffmpeg-2.7.2
