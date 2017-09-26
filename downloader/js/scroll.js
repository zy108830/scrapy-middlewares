﻿
var head = document.getElementsByTagName('head')[0];
var script = document.createElement('script');
script.type = 'text/javascript';
script.src = 'https://apps.bdimg.com/libs/jquery/2.0.3/jquery.min.js';
head.appendChild(script);

script.onload = function () {
    $(function () {
        var newlen = 0, scroll_load_time = 3000;
        loadingMore();

        function loadingMore() {
            var scrollTop = $(window).scrollTop(), oldlen = getItemLength();
            $(window).scrollTop(scrollTop + 5000);
            setTimeout(function () {
                newlen = getItemLength();
                if (newlen > oldlen) {
                    loadingMore();
                } else {
                    loadingCompleteCallback();
                }
            }, scroll_load_time);
        }

        function loadingCompleteCallback() {
            $('body').attr('has_more', 0);
        }

        function getItemLength() {
            //需要自行定制自己的itemsSelector
            return $('.relatedFeed').find('.item').length;
        }
    });
};