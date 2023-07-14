
raspberry 
	para arracar coloque dentro de /etc/rs.local la siguiente linea
		nohup /home/roacho/python/doppler/start.sh &
	
	para checar el estatus es 
		systemctl status rc-local.service
	
	para agregar el usuario a dialog y tener acceos a los serial port	
		sudo usermod -a -G dialout $USER
		
	para ver los serial port podemos usar
		dmesg | grep tty
		
	para poder correr bien y controlar el nohup sae creo un sh con el siuguiente codigo
		python3 /ruta/ops.radar.py
		
		
	se requiere instala en poython serial opencv-python opencv-python-headless
	
	cuando baje cambios del node.js borrar carpeta modulos y darle npm install
	
	
	para instalar opencv usar estas instrucciones (https://www.piwheels.org/project/opencv-contrib-python/)
	
	sudo apt install libwayland-cursor0 libxfixes3 libva2 libdav1d4 libavutil56 libxcb-render0 libwavpack1 libvorbis0a libx264-160 libx265-192 libaec0 libxinerama1 libva-x11-2 libpixman-1-0 libwayland-egl1 libzvbi0 libxkbcommon0 libnorm1 libatk-bridge2.0-0 libmp3lame0 libxcb-shm0 libspeex1 libwebpmux3 libatlas3-base libpangoft2-1.0-0 libogg0 libgraphite2-3 libsoxr0 libatspi2.0-0 libdatrie1 libswscale5 librabbitmq4 libhdf5-103-1 libharfbuzz0b libbluray2 libwayland-client0 libaom0 ocl-icd-libopencl1 libsrt1.4-gnutls libopus0 libxvidcore4 libzmq5 libgsm1 libsodium23 libxcursor1 libvpx6 libavformat58 libswresample3 libgdk-pixbuf-2.0-0 libilmbase25 libssh-gcrypt-4 libopenexr25 libxdamage1 libsnappy1v5 libsz2 libdrm2 libxcomposite1 libgtk-3-0 libepoxy0 libgfortran5 libvorbisenc2 libopenmpt0 libvdpau1 libchromaprint1 libpgm-5.3-0 libcairo-gobject2 libavcodec58 libxrender1 libgme0 libpango-1.0-0 libtwolame0 libcairo2 libatk1.0-0 libxrandr2 librsvg2-2 libopenjp2-7 libpangocairo-1.0-0 libshine3 libxi6 libvorbisfile3 libcodec2-0.9 libmpg123-0 libthai0 libudfread0 libva-drm2 libtheora0
	sudo pip3 install opencv-contrib-python
	
	
	
	https://github.com/shadowdevelop/FotoMultas
	
	https://github.com/shadowdevelop/fotomultaconfig