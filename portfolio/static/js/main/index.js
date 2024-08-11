$(document).ready(function() {
    console.log('index')

    // hide and show text every 5sec
    function blinkAndToggle(current, next) {
        let blinks = 4;  // Number of blinks
        let blinkSpeed = 200; // Speed of each blink (in milliseconds)
        
        function blink(count) {
            if (count > 0) {
                current.fadeOut(blinkSpeed, function() {
                    current.fadeIn(blinkSpeed, function() {
                        blink(count - 1);
                    });
                });
            } else {
                current.fadeOut(2000, function() {
                    next.fadeIn(2000);
                });
            }
        }
        
        blink(blinks);
    }

    function toggleHeadings() {
        if ($("#name").is(":visible")) {
            blinkAndToggle($("#name"), $("#career"));
        } else {
            blinkAndToggle($("#career"), $("#name"));
        }
    }

    setInterval(toggleHeadings, 10000); // Call the function every 10 seconds

    function switchTab(activeTab, activeContent) {
        
    } 
    
    // About me interactivity
    $('#skills').click(function() {
        console.log('skill click')
        $('#skills').addClass('actives');
        $('#cert').removeClass('actives');
        $('#edu').removeClass('actives');
        $('#skill-content').show();
        $('#edu-content').hide();
        $('#cert-content').hide();
    });

    $('#edu').click(function() {
        console.log('education click')
        $('#edu').addClass('actives');
        $('#skills').removeClass('actives');
        $('#cert').removeClass('actives');
        $('#skill-content').hide();
        $('#edu-content').show();
        $('#cert-content').hide();
    });

    $('#cert').click(function() {
        console.log('cert click')
        $('#cert').addClass('actives');
        $('#skills').removeClass('actives');
        $('#edu').removeClass('actives');
        $('#skill-content').hide();
        $('#edu-content').hide();
        $('#cert-content').show();
    });


});