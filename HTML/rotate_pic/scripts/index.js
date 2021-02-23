window.onload = function () {


    var arr = document.querySelector(".arrow");
    li = document.querySelector('.container').children[0].children;

    flag = true;

    arr.addEventListener('mouseover', function () {
        animate(this, { 'opacity': 1 })
    });

    arr.addEventListener('mouseout', function () {
        animate(this, { 'opacity': 0 })
    });

    arr.children[0].addEventListener('click', function () {
        if (flag) {
            flag = false;
            config.push(config.shift());
            assign();
        }

    });

    arr.children[1].addEventListener('click', function () {
        if (flag) {
            flag = false;
            config.unshift(config.pop());
            assign();
        }
    });



    config = [
        {
            "width": 400,
            "top": 20,
            "left": 50,
            "opacity": .2,
            "zIndex": 2
        },
        {
            "width": 600,
            "top": 70,
            "left": 0,
            "opacity": .8,
            "zIndex": 3
        },
        {
            "width": 800,
            "top": 100,
            "left": 250,
            "opacity": 1,
            "zIndex": 4
        },
        {
            "width": 600,
            "top": 70,
            "left": 700,
            "opacity": .8,
            "zIndex": 3
        },
        {
            "width": 400,
            "top": 20,
            "left": 850,
            "opacity": .2,
            "zIndex": 2
        },
    ];

    assign();

}

function assign() {
    for (var i = 0; i < li.length; i++)
        animate(li[i], config[i], function () { flag = true });
}




/******************** animate ********************************/

function animate(obj, attrobj, callback, time_ms = 15) {
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        var flag = true;
        for (var k in attrobj) {
            if (k == "opacity") {
                var leader = getstyle(obj, k) * 100;
                var target = attrobj[k] * 100;
                var step = (target - leader) / 10;
                step = step > 0 ? Math.ceil(step) : Math.floor(step);
                leader += step;
                obj.style[k] = leader / 100;
                if (target !== leader)
                    flag = false;
            } else if (k == "zIndex") {
                obj.style.zIndex = attrobj[k];
            }
            else {
                var leader = parseInt(getstyle(obj, k)) || 0;
                var target = attrobj[k];
                var step = (target - leader) / 10;
                step = step > 0 ? Math.ceil(step) : Math.floor(step);
                leader += step;
                obj.style[k] = leader + 'px';
                if (target !== leader)
                    flag = false;
            }
        }
        if (flag) {
            clearInterval(obj.timer);
            if (callback) callback();
        }

    }, time_ms)
}


function getstyle(obj, attr) {
    return getComputedStyle(obj)[attr];
}