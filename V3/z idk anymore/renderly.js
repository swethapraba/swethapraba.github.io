// This makes the code below execute immediately, but doesn't allow the vars we declared to "leak" out of the scope or
// let other javascript loaded accidentally change something. This is called IIFE, immediately invoked function expression
(function() {

    // Array to store the message object that contains the iframe created by the iframeResizer library
    var messages = [];

    // This value is given to the jquery scroll
    var SCROLL_VARIABLE = 3000;
    var SCROLL_STYLE = "swing";

    // indicates that we already scrolled
    var didScroll = false;

    // if there is an hash
    if(window.location.hash){

        // Prevent automatic window jumping
        scroll(0,0);
    }

    // Should only should message if iframes before this are loaded, check by seeing if everything is setup
    function shouldSendMessage(index, array) {
        for (var i = 0; i <= index; i++) {
            var value = array[i];

            // undefined checks that an object was placed inside, value.iframe prevents errors from being throw
            // value.iframe.iFrameResizer checks that the object was properly initialized
            if (value === undefined || value.iframe === undefined || value.iframe.iFrameResizer === undefined) {
                return false;
            }
        }
        return true;
    }

    // compute percentage and send the message to all iframes
    function sendMessages() {
        messages.forEach( function (value, index, array) {



            /*
             * Before passing message, ensure prior iframe has loaded, if not ignore
             */

            if (!shouldSendMessage(index, array)) {
                return;
            }


            /*
             * Start of message notification
             */

            // Get the message object created by the iframe resizer library
            var message = value;

            // Get the iframe from the id
            var iframeId = message.iframe.id;
            var $iframe = $("#" + iframeId );

            // Fix blank bug attempt
            $iframe.onload = function () {
                message.iframe.iFrameResizer.resize();
            };

            // iframe
            var iframeHeight = parseFloat(message.height);
            var iframeTop = parseFloat($iframe.offset().top);
            var iframeBottom = parseFloat(iframeTop) + parseFloat(iframeHeight);

            // Viewport
            var viewHeight = parseFloat($(window).innerHeight());
            var viewTop = parseFloat($(window).scrollTop());
            var viewBottom = parseFloat(viewHeight + $(window).scrollTop());


            /*
             * Scroll ratio
             */

            // What ratio of the scroll to the top of the iframe is
            var scrollRatio = (viewBottom - iframeTop) / iframeHeight;


            /*
             * Vertical display ratio
             */

            // Overlap of viewport against iframe. WARNING: Does not mention if overlap is at bottom or top
            var verticalDisplayRatio = 0;

            // Viewport is above or at the iframe
            if (viewTop <= iframeTop && viewBottom <= iframeBottom) {
                var numerator = viewBottom - iframeTop;
                verticalDisplayRatio = numerator / iframeHeight;

                // Iframe encompassses the viewport
            } else if (viewTop > iframeTop && viewBottom < iframeBottom) {
                var numerator = viewHeight;
                verticalDisplayRatio = numerator / iframeHeight;

                // Viewport is below the iframe
            } else if (viewBottom > iframeBottom) {
                var numerator = iframeBottom - viewTop;
                verticalDisplayRatio = numerator / iframeHeight;
            }

            // Adjust, coverage should never be less than 0 or greater than 1
            if (verticalDisplayRatio < 0) {
                verticalDisplayRatio = 0;
            } else if (verticalDisplayRatio > 1) {
                verticalDisplayRatio = 1;
            }

            // Create jsonMessage with properties(messages must be passed in json format)
            var jsonMessage =
                '{"scrollRatio":' + scrollRatio +
                ', "verticalDisplayRatio":' + verticalDisplayRatio + "}";

            // Send this data to this iframe
            message.iframe.iFrameResizer.sendMessage(jsonMessage, []);



            //  Send this event to indicate that this iframe is fully loaded and ready to be scrolled to
            $(document).trigger("readyForScroll", iframeId);
        });
    }


    iFrameResize({
        log: false,
        bodyMargin: 0,
        bodyPadding: 0,
        enableInPageLinks: true,
        checkOrigin: false,
        onResized: function (messageData) {

            // Get the iframe jquery object, which is [iframe#header, context: document, selector: "#header"]
            var $iframe = $("#" + messageData.iframe.id);

            // Get what order this should be displayed in
            var displayOrder = $iframe.attr("data-displayOrder");

            // Put messageData in the same order as displayOrder
            messages[displayOrder] = messageData;

            // Notify all child iframes
            sendMessages();
        },

        // Received message from child
        onMessage: function (messageData) {

            // messageData has iframe,message
            var jsonMessage = JSON.parse(messageData.message);

            // Example of doing a certain action given a message
            if (jsonMessage.action === "scroll") {

                // the id of the child iframe that messaged this
                var targetId = jsonMessage.target;

                // Do the scrolling
                $('html, body').animate({
                    scrollTop: $(targetId).offset().top
                }, SCROLL_VARIABLE, SCROLL_STYLE);
            }
        }
    });



    //
    // Event listeners
    //

    // When we get the scroll event
    $(window).on("scroll", function(){

        // send the messages to the iframes as some iframes need the values for scroll based animations
        sendMessages();
    });



    // When a iframe is fully loaded it fires the ready for scroll event. We check to see if there is a hash in the url,
    // if there is a hash and the hash is the same as the iframe that is ready to scroll, scroll to that iframe
    $(document).on('readyForScroll', function (event, iframeId) {

        // Check to see if we already did the scrolling
        if( !didScroll ){

            var hash = window.location.hash;

            // if there is a hash
            if( hash ){

                // If this # is the same as the one that is ready to be scrolled to
                if( hash === ("#" + iframeId) ) {

                    // set that we did the scroll so the page is not stuck
                    didScroll = true;

                    // Do the scrolling
                    $('html, body').animate({
                        scrollTop: $(hash).offset().top
                    }, SCROLL_VARIABLE, SCROLL_STYLE);
                }
            }
        }
    });

})();