$(document).ready(function () {
  
    $("#owl-demo1").owlCarousel({
        items: 3,
        margin: 10,
        dots: false,
        loop:true,
        autoplay: 2000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 3,
                nav: false,
                dots:true
            },
            700: {
                items: 4,
                nav: false
            },
            1024: {
                items: 4,
                nav: true,
                loop: false
            },
            1500:{
                items: 4,
                nav: true,
                loop: false
            }
        }
    });      
    $("#owl-demo2").owlCarousel({
        items: 3,
        margin: 10,
        autoplay: 2000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2,
                nav: false
            },
            767: {
                items: 3,
                nav: false
            },
            1024: {
                items: 3,
                nav: false,
                loop: false
            },
            1500:{
                items: 4,
                nav: false,
                loop: false
            }
        }
    });
    $('#owl-demo3').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        autoplay:2000,
        dots:true,
        responsive:{
            0:{
                items:3
            },
            600:{
                items:4
            },
            1000:{
                items:6,
                dots:true,
            }
        }
    })
});


var speed = 10;

/* Call this function with a string containing the ID name to
 * the element containing the number you want to do a count animation on.*/
function incEltNbr(id) {
  elt = document.getElementById(id);
  endNbr = Number(document.getElementById(id).innerHTML);
  incNbrRec(0, endNbr, elt);
}

/*A recursive function to increase the number.*/
function incNbrRec(i, endNbr, elt) {
  if (i <= endNbr) {
    elt.innerHTML = i;
    setTimeout(function() {//Delay a bit before calling the function again.
      incNbrRec(i + 1, endNbr, elt);
    }, speed);
  }
}

/*Function called on button click*/
 /*Call this funtion with the ID-name for that element to increase the number within*/

(function ($) {	

	$.fn.searchBox = function(ev) {

		var $searchEl = $('.search-elem');
		var $placeHolder = $('.placeholder');
		var $sField = $('#search-field');

		if ( ev === "open") {
			$searchEl.addClass('search-open')
		};

		if ( ev === 'close') {
			$searchEl.removeClass('search-open'),
			$placeHolder.removeClass('move-up'),
			$sField.val(''); 
		};

		var moveText = function() {
			$placeHolder.addClass('move-up');
		}

		$sField.focus(moveText);
		$placeHolder.on('click', moveText);
		
		$('.submit').prop('disabled', true);
		$('#search-field').keyup(function() {
	        if($(this).val() != '') {
	           $('.submit').prop('disabled', false);
	        }
	    });
	}	

}(jQuery));

$('.search-btn').on('click', function(e) {
	$(this).searchBox('open');
	e.preventDefault();
});

$('.close').on('click', function() {
	$(this).searchBox('close');
});

