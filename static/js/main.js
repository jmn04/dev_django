console.log("main.js load");
document.getElementById('FormFile').addEventListener('change', handleFileSelect, false);
function handleFileSelect(event) {
	var area = document.getElementById('file');
	area.insertAdjacentHTML('afterend','<div id="preview"></div>');
	

	var files = event.target.files;
	var reader = new FileReader();
    var f = files[0]
	reader.onload = (function(theFile) {
		return function(event) {
			// styleHeightの値に合わせて、footer.style.bottomを変更のこと。
			var styleHeight = "500px";
			var footer = document.getElementsByTagName("footer").item(0);
			var preview = document.createElement('div');

			preview.classList.add('d-block');
			preview.innerHTML = ['<img class="img-thumbnail d-block mx-auto" src="', event.target.result,'" title="', escape(theFile.name), '" style="height: styleHeight;" /><div class="small text-muted text-center">', escape(theFile.name),'</div>'].join('');// 画像では画像のプレビューとファイル名の表示
           document.getElementById('preview').appendChild(preview);
			footer.style.bottom=`calc(-${styleHeight} - ${parseInt(footer.clientHeight) + 'px'})`;
        };
    })(f);
    reader.readAsDataURL(f);
};

// 取消ボタンでリセット
document.getElementById('btnResetFile').addEventListener('click', function(event) {
	document.getElementById('FormFile').value = '';
	document.getElementById('preview').remove();
}, false);