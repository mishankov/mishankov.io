BLOCK_LIST = ['aboutme', 'job', 'github', 'instagram', 'soundcloud', 'footer'];
CURRENT_POSITION = '';


window.onload = function() {
	CURRENT_POSITION = BLOCK_LIST[0];
	// CURRENT_POSITION = 'soundcloud';
	location.hash = CURRENT_POSITION;

	// for (let i=0; i<BLOCK_LIST.length; i++) {
	// 	element = document.getElementsByClassName('hp-'+BLOCK_LIST[i])[0];
	// 	element.addEventListener("wheel", function (e){
	// 		if (i!=0 && e.deltaY<0) {
	// 			CURRENT_POSITION = BLOCK_LIST[i-1]
	// 			scrollToBlock(CURRENT_POSITION);
	// 		}

	// 		if (i!=BLOCK_LIST.length-1 && e.deltaY>0) {
	// 			CURRENT_POSITION = BLOCK_LIST[i+1]
	// 			scrollToBlock(CURRENT_POSITION);
	// 		}

	// 		e.preventDefault();
	// 	}, false);

	// 	console.log(element);
	// }
}

function scrollToBlock(block) {
	console.log(block)
	location.hash = block
}