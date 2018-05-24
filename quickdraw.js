var quickDraw = require('quickdraw.js');

const categories = ['airplane', 'apple', 'banana', 'basket', 'bee', 'bench', 'bicycle', 'bus', 'butterfly', 'cat', 'chair',
              'cloud', 'cow', 'cup', 'dog', 'duck', 'horse', 'house', 'moon', 'pig', 'rabbit', 'sheep', 'streetlight',
              'sun', 'table', 'tree', 'truck', 'umbrella'];

var cate_counts = [490, 125, 49, 73, 218, 264, 46, 108, 168, 137, 500, 51, 175, 62, 230, 92, 479, 234, 44, 168, 168, 170,
                69, 139, 692, 687, 79, 19];

for (var i in categories) {
	var cate = categories[i];
	var cnt = cate_counts[i];
	quickDraw.import(cate, cnt, 128);
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

setTimeout(exportJson, 60000);
