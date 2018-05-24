var quickDraw = require('quickdraw.js');
//var set = quickDraw.set(100, ['car', 'airplane', 'bicycle']);
//cars = quickDraw.import('car', 100);

const categories = ['airplane', 'apple', 'banana', 'basket', 'bee', 'bench', 'bicycle', 'bus', 'butterfly', 'cat', 'chair',
	'cloud', 'cow', 'cup', 'dog', 'duck', 'house', 'moon', 'pig', 'rabbit', 'sheep', 'streetlight',
	'sun', 'table', 'tree', 'duck', 'umbrella'];

var cate_counts = [490, 125, 49, 73, 218, 264, 46, 108, 168, 137, 500, 51, 175, 62, 230, 92, 479, 234, 44, 168, 168, 170,
	69, 139, 692, 687, 79, 19];

console.log('Start');

for (var i in categories) {
	var cate = categories[i];
	var cnt = cate_counts[i];
	quickDraw.import(cate, cnt);
}

function exportJson() {
	for (var i in categories) {
		var cate = categories[i];
		var cnt = cate_counts[i];
		var dataSet = quickDraw.set(cnt, [cate]);
		var fs = require('fs');
		fs.writeFile(cate + ".json", JSON.stringify(dataSet), function (err) {
			if (err) {
				console.log(err);
			} else {
				console.log("completed");
			}
		});
	}
}

setTimeout(exportJson, 20000);
