$(document).ready(function(){
	
	$('ul.tab li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tab li').removeClass('current');
		$('.containers').removeClass('active');

		$(this).addClass('current');
		$("#"+tab_id).addClass('active');
	})

})

$('.tab-1-1-btn_answer').on('click',function(){
	//버튼 색 제거,추가
	$('.tab-1-1-btn_answer').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab-1-1-btn_answer').index(this);
	
	$('.tab_box_1-1').hide();
	$('.tab_box_1-1').eq(idx).show();
  });


$('.tab-1-2-btn_answer').on('click',function(){
	//버튼 색 제거,추가
	$('.tab-1-2-btn_answer').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab-1-2-btn_answer').index(this);
	
	$('.tab_box_1-2').hide();
	$('.tab_box_1-2').eq(idx).show();
  });

$('.tab-1-3-btn_answer').on('click',function(){
	  //버튼 색 제거,추가
	  $('.tab-1-3-btn_answer').removeClass('on');
	  $(this).addClass('on')
	  
	  //컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	  var idx = $('.tab-1-3-btn_answer').index(this);
	  
	  $('.tab_box_1-3').hide();
	  $('.tab_box_1-3').eq(idx).show();
	});
  
$('.tab-2-1-btn_answer').on('click',function(){
	//버튼 색 제거,추가
	$('.tab-2-1-btn_answer').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab-2-1-btn_answer').index(this);
	
	$('.tab_box_2-1').hide();
	$('.tab_box_2-1').eq(idx).show();
	});


$('.tab-2-2-btn_answer').on('click',function(){
	//버튼 색 제거,추가
	$('.tab-2-2-btn_answer').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab-2-2-btn_answer').index(this);
	
	$('.tab_box_2-2').hide();
	$('.tab_box_2-2').eq(idx).show();
	});

$('.tab-2-3-btn_answer').on('click',function(){
		//버튼 색 제거,추가
		$('.tab-2-3-btn_answer').removeClass('on');
		$(this).addClass('on')
		
		//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
		var idx = $('.tab-2-3-btn_answer').index(this);
		
		$('.tab_box_2-3').hide();
		$('.tab_box_2-3').eq(idx).show();
	});
		
$('.tab-3-1-btn_answer').on('click',function(){
	//버튼 색 제거,추가
	$('.tab-3-1-btn_answer').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab-3-1-btn_answer').index(this);
	
	$('.tab_box_3-1').hide();
	$('.tab_box_3-1').eq(idx).show();
	});


$('.tab-3-2-btn_answer').on('click',function(){
	//버튼 색 제거,추가
	$('.tab-3-2-btn_answer').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab-3-2-btn_answer').index(this);
	
	$('.tab_box_3-2').hide();
	$('.tab_box_3-2').eq(idx).show();
	});

$('.tab-3-3-btn_answer').on('click',function(){
	//버튼 색 제거,추가
	$('.tab-3-3-btn_answer').removeClass('on');
	$(this).addClass('on')
	
	//컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
	var idx = $('.tab-3-3-btn_answer').index(this);
	
	$('.tab_box_3-3').hide();
	$('.tab_box_3-3').eq(idx).show();
});