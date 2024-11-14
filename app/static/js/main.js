(function ($) {
    "use strict";

    // Initiate the wowjs
    new WOW().init();


    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });
    // $("#contact").on("submit", (e) => {
    //     e.preventDefault();
    //     const data = {
    //         'name': $('input[name=name]').val(),
    //         'email': $('input[name=email]').val(),
    //         'cname': $('input[name=cname]').val(),
    //         'cage': $('input[name=cage]').val(),
    //         'content': $('textarea[name=content]').val(),
    //         'csrfmiddlewaretoken': '{{ csrf_token }}'
    //     };
    //     $.post("http://127.0.0.1:8000/messages/receive_message/", data, () => {
    //         console.log("all is okay");
    //     });
    
    //     e.target.reset();
    //     });

})(jQuery);

// $.post("/receive_message/", data)
// .done(() => {
//     console.log("Form submission successful");
//     alert("Your message has been sent!");
// })
// .fail(() => {
//     console.error("Form submission failed");
//     alert("There was an error. Please try again.");
// });
// e.target.reset();
// });


$(document).ready(function () {
    $('#contactForm').on('submit', function (e) {
        e.preventDefault();
        
        const formData = {
            name: $('#name').val(),
            email: $('#email').val(),
            message: $('#message').val(),
        };
        
        $.ajax({
            url: 'process_form.php',
            type: 'POST',
            data: formData,
            success: function (response) {
                $('#formResponse').html(response);
                $('#contactForm')[0].reset();
            },
            error: function () {
                $('#formResponse').html('<p class="text-danger">There was an error submitting your message.</p>');
            }
        });
    });
});
