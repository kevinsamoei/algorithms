function is_isogram(word){
	if (typeof(word) === "string")
		throw "Argument should be a string";
	else if(word === ' ')
		return word, false;
	else
		var word = word.toLower();
		for (var i = word.length; i >= 0; i--) {
			if(word[i] === 
		}