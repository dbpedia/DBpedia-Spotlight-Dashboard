echo "File: $1"
while read line;
do
	url=`echo "$line" | cut -d' ' -f1 | cut -d'<' -f2 | cut -d'>' -f1`
	if ! wget -q --method=HEAD $url; then
		echo $line >> invalid_instance_types
	else
		echo $line >> valid_instance_types
	fi
done < "$1"
echo "$1 file URLs completed"