function pulse() {
    $('#seventyfive').animate({
        width: 300, height: 300, 
        opacity: 0.5
    }, 700, function() {
        $('#seventyfive').animate({
            width: 320, height: 320, 
            opacity: 1
        }, 700, function() {
            pulse();
        });
    }); 
};

pulse();