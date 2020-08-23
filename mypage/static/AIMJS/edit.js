$(document).ready(function(){
	
	$('ul.tab li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tab li').removeClass('current');
		$('.containers').removeClass('active');

		$(this).addClass('current');
		$("#"+tab_id).addClass('active');
	})

})

$('.tab_menu_btn').on('click',function(){
	//버튼 색 제거,추가
	$('.tab_menu_btn').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab_menu_btn').index(this);
	
	$('.tab_box').hide();
	$('.tab_box').eq(idx).show();
  });