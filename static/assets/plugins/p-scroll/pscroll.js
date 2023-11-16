(function($) {
    "use strict";
    
    try {
        const ps = new PerfectScrollbar('.app-sidebar', {
            useBothWheelAxes: true,
            suppressScrollX: true,
            suppressScrollY: false,
        });
    } catch { }

    //P-scrolling
})(jQuery);