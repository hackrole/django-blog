dir=/var/www/blog

all: ctags  etags filenametags cscope
	echo "succus"

ctags:
	ctags -R -o ctags ${dir}

etags:
	ctags -e -R ${dir}

cscope:
	find ${dir} -type f -regex '.*\.\(py\|js\)' > cscope.files
	cscope -bq

filenametags:
	echo -e "!_TAG_FILE_SORTED\t2\t2/2=foldcase/" > filenametags
	find ${dir} -not -regex '.*\.\(png\|gif\|jpg\)' -type f -printf "%f\t%p\t0\n" | sort -f >> filenametags
