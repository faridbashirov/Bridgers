// $(function () {
//   var $grid = $('.grid').isotope({
//       itemSelector: 'article',
//       filter: '*'
//   });

//   // filter buttons
//   $('.filters-button-group').on('click', 'button', function () {
//       var filterValue = $(this).attr('data-filter');
//       $grid.isotope({ filter: filterValue });
//   });
//   $('.button-group').each(function (i, buttonGroup) {
//       var $buttonGroup = $(buttonGroup);
//       $buttonGroup.on('click', 'button', function () {
//           $buttonGroup.find('.is-checked').removeClass('is-checked');
//           $(this).addClass('is-checked');
//       });
//   });
// });



// $('.wrapper').on('click', "#share", function(e) {
//     var _this = $('.wrapper');
//     if (_this.hasClass('in')) {
//       animateOut.play();
//       _this.removeClass('in');
//       return;
//     }
//     animateIn.play();
//     _this.addClass('in');
//   });
  
//   var animateIn = anime({
//     targets: '.icon',
//     delay: function(el, index) {
//       return index * 400;
//     },
//     translateX: function(el, index) {
//       return (index - 1) * 50;
//     },
//     translateY: '-50px',
//     duration: 400,
//     loop: false,
//     easing: 'easeOutQuart',
//     autoplay: false
//   });
  
//   var animateOut = anime({
//     targets: '.icon',
//     delay: function(el, index) {
//       return index * 100;
//     },
//     translateY: ['-50px', '0px'],
//     translateX: function(el, index) {
//       var current = (index - 1) * 50;
//       return [current + 'px', '0px'];
//     },
//     duration: 300,
//     loop: false,
//     easing: 'easeOutQuart',
//     autoplay: false
//   });

  