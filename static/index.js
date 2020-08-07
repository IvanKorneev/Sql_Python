$(document).ready(function () {

    console.log('Hi from jquery');

    Handlebars.registerHelper('eachProperty', function(context, options) {
        var ret = "";
        for(var prop in context)
        {
            ret = ret + options.fn({property:prop,value:context[prop]});
        }
        return ret;
    });

    // $.getJSON('../static/data/data.json', function (data) {
    //     // Step 1: get the template:
    //     var template = $("#itemTemplate").html();
    //     console.log(template);
    //     // Step 2: Handlebars compiles the template into a callable function
    //     var renderer = Handlebars.compile(template);
    //     console.log(renderer);
    //     // Step 3: call the compiled function with the template data
    //     var result = renderer(data);
    //     console.log(result)
    //     // Step 4: Puth the rendered template into HTML:
    //     $("#container").html(result);
    // });

    

    $("#submit").click(function () {
        var sqlQuery = $('#sqlfield').val();
        var data = $.post('/json', {"query": sqlQuery}, function (data, status){
            // console.log( typeof data)
            // console.log(data)
            // console.log(sqlQuery)
            // Step 1: get the template:
            var template = $("#itemTemplate").html();
            // Step 2: Handlebars compiles the template into a callable function
            var renderer = Handlebars.compile(template);
            // Step 3: call the compiled function with the template data
            var result = renderer(data);
            // console.log(result)
            // Step 4: Puth the rendered template into HTML:
            $("#container").html(result);
        });
    });
});