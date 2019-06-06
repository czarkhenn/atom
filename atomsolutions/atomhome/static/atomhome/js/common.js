<!-- Logo Loop -->
$(document).ready( function(){
	var timestamp = new Date().getTime();
	$('.logo_gifanime').attr('src', '/images/animatedLogo-Atom.gif' + '?' + timestamp);
});
<!-- Logo Loop -->

<!-- ANKER -->
$(function(){
	$('a[href^=#]').click(function(){
		var speed = 500;
		var href= $(this).attr("href");
		var target = $(href == "#" || href == "" ? 'html' : href);
		var position = target.offset().top;
		$("html, body").animate({scrollTop:position}, speed, "swing");
		return false;
	});
});
<!-- ANKER -->

<!-- modal menu -->
	$(function(){
		$(".menu-open").on("click", function(e) {
			e.preventDefault();
			$(".modal-menu").fadeToggle();
		});
		$(".menu-close").on("click", function(e) {
			e.preventDefault();
			$(".modal-menu").fadeOut();
		});
		$(".modal-menu ul.nav li a").on("click", function(e) {
			e.preventDefault();
			$(".modal-menu").fadeOut();
		});
		return false;
	});
<!-- modal menu -->

<!-- countup -->
$(function(){
	var countElm = $('.count'),
	countSpeed = 20;

	countElm.each(function(){
		var self = $(this),
		countMax = self.attr('data-num'),
		thisCount = self.text(),
		countTimer;

		function timer(){
			countTimer = setInterval(function(){
				var countNext = thisCount++;
				self.text(countNext);

				if(countNext == countMax){
					clearInterval(countTimer);
				}
			},countSpeed);
		}
		timer();
	});

});
<!-- countup -->

<!-- ACTION -->
$(function(){
  $('.movLink').addClass('moveDef');
  $(window).scroll(function(){
    $(".cts-mov .col").each(function(){
      var imgPos = $(this).offset().top;    
      var scroll = $(window).scrollTop();
      var windowHeight = $(window).height();
      if (scroll > imgPos - windowHeight + windowHeight/1.8){
        $(this).find(".movLink").removeClass('moveDef');
      } else {
        $(this).find(".movLink").addClass('moveDef');
      }
    });
  });
});
$(function(){
  $('.movData').addClass('moveDef');
  $(window).scroll(function(){
    $(".cts-mov .col").each(function(){
      var imgPos = $(this).offset().top;    
      var scroll = $(window).scrollTop();
      var windowHeight = $(window).height();
      if (scroll > imgPos - windowHeight + windowHeight/1.6){
        $(this).find(".movData").removeClass('moveDef');
      } else {
        $(this).find(".movData").addClass('moveDef');
      }
    });
  });
});
<!-- ACTION -->

<!-- News -->
$(function () {
  $('time').each(function(){
    // 現在日時
    var current = new Date();
    // 14日（2週間）前のミリ秒
    var range_ms = current.getTime() - (7 * 24 * 60 * 60 * 1000);

    // 更新日時
    var modified = new Date($(this).attr('datetime'));
    // 更新日時のミリ秒
    var modified_ms = modified.getTime();

    if (range_ms < modified_ms){
      $(this).after('<p></p>');
    }
  });
});
<!-- News -->

$('#if_new').on('click',function(){
	$.cookie('if_new', '2019-05-23', {expires: 365, path:'/'});
});

$(document).ready( function(){
	if ($.cookie("if_new") !== '2019-05-23')
		$("#new").css({
			"display": "block"
		});
});
