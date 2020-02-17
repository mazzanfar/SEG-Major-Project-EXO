window.commentFuncs = {
    removeCommentForm: function (comment) {
        $('#' + comment + '>.bs-callout-main').next().remove();
    },
    toggleForm: function (url, $placeAfter, params, $toggle, onSuccessFunc) {
        if ($toggle === undefined || !$toggle.hasClass('clicked')) {
            // load a form a given url
            $.get(url, params, function (data) {
                $placeAfter.after(data);
                if (typeof onSuccessFunc === 'function')
                    onSuccessFunc();
            });
        }
        else // remove the form
            $placeAfter.next().remove();
        $toggle.toggleClass('clicked');
    },
    toggleCommentForm: function (comment, toggle, url) {
        //url = urljoin(url, comment);
        console.log(comment)
        var $placeAfter = $('#' + comment);
        console.log($placeAfter)
        window.commentFuncs.toggleForm(url, $placeAfter, {}, $(toggle));
    },
};
